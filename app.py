import csv
from datetime import datetime
from io import StringIO

from bokeh.embed import file_html
from bokeh.models import ColumnDataSource, value
from bokeh.plotting import figure
from bokeh.resources import CDN

from flask import Flask, Response, request, jsonify

import pandas as pd
import prometheus_client
from prometheus_client.core import CounterMetricFamily, REGISTRY

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from openapi_client import LaunchesApi


class SpacexCollector(object):
    def __init__(self):
        self.__cache_validity = 720
        self.__last_cache_update = None
        self.__lapi = LaunchesApi()
        self.__launches = None

    def collect(self):
        c = CounterMetricFamily(
            "performed_launches",
            "Total performed launches",
            labels=[
                "mission",
                "year",
                "success",
                "cores_reused"
            ]
        )

        if self.__last_cache_update:
            cache_expired = (datetime.utcnow() - self.__last_cache_update).seconds / 60 >= self.__cache_validity
        else:
            cache_expired = True

        if cache_expired:
            self.__launches = self.__lapi.past_launches()
            self.__last_cache_update = datetime.utcnow()

        performed = 0
        for launch in self.__launches:
            cores_reused = 0
            for core in launch.rocket.first_stage.cores:
                if core.reused:
                    cores_reused += 1

            performed += 1
            c.add_metric(
                labels=[
                    launch.mission_name,
                    launch.launch_year,
                    str(launch.launch_success),
                    str(cores_reused),
                ],
                value=performed,
                timestamp=launch.launch_date_unix,
            )

        yield c


REGISTRY.register(SpacexCollector())

app = Flask(__name__)
# Add prometheus wsgi middleware to route /api/prom/metrics requests
app_dispatch = DispatcherMiddleware(app, {
    "/api/prom/metrics": prometheus_client.make_wsgi_app()
})


@app.route("/api/metrics")
def get_metrics():
    metrics = REGISTRY.collect()
    metrics_names = []
    for metric in metrics:
        metrics_names.append(metric.samples[0].name)

    return jsonify(metrics_names)


@app.route("/api/csv/<metric>")
def get_file(metric):
    restricted_registry = REGISTRY.restricted_registry([metric])
    samples = restricted_registry.collect()[0].samples
    labels = sorted(samples[0].labels.keys())

    with StringIO() as f:
        writer = csv.writer(f)
        writer.writerow(["", "name", "timestamp", "value"] + labels)
        idx = 0
        for sample in samples:
            line = [idx, sample.name, sample.timestamp, sample.value]
            for label in labels:
                line.append(sample.labels.get(label, ""))
            writer.writerow(line)
            idx += 1

        response = Response(f.getvalue(), mimetype="text/csv")
        response.headers.set(
            "Content-Disposition",
            "attachment",
            filename="{0}.csv".format(metric)
        )
        return response


@app.route("/")
def index():
    launches_csv_url = request.host_url + "api/csv/performed_launches_total"
    data = pd.read_csv(
        launches_csv_url,
        index_col=0
    ).dropna()

    plot = figure(
        plot_width=800,
        title="Launches per year",
        toolbar_location="above",
        tools="save,box_zoom,reset,wheel_zoom,tap",
    )

    success_gb = data.groupby(["year", "success"]).size()
    success_df = success_gb.to_frame(name="size").reset_index()
    success_pt = pd.pivot_table(
        success_df,
        index="year",
        columns="success"
    )
    success_pt.fillna(value=0, inplace=True)
    success_pt_column_names = ["Failure", "Success"]
    success_pt.columns = success_pt_column_names
    success_csd = ColumnDataSource(data=success_pt)

    plot.vbar_stack(
        success_pt_column_names,
        x="year",
        width=0.9,
        source=success_csd,
        color=[
            "#ff0000",
            "#008000"
        ],
        legend=[value(x) for x in success_pt_column_names]
    )

    core_reuse_gb = data.groupby("year", as_index=True).agg({"cores_reused": "sum"})
    core_reuse_cds = ColumnDataSource(core_reuse_gb)

    plot.step(
        y="cores_reused",
        x="year",
        source=core_reuse_cds,
        color="#000000",
        legend="Cores Reused"
    )

    plot.y_range.start = 0
    plot.x_range.range_padding = 1
    plot.xgrid.grid_line_color = "gray"
    plot.axis.minor_tick_line_color = None
    plot.outline_line_color = None
    plot.xaxis.axis_label = "Year"
    plot.yaxis.axis_label = "Launches"
    plot.legend.location = "top_left"
    plot.legend.orientation = "horizontal"

    return file_html(plot, CDN, title="is SpaceX ok")


if __name__ == "__main__":
    run_simple(
        "0.0.0.0",
        8050,
        app_dispatch,
        processes=3
    )
