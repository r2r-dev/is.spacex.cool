### Description
This project aims to collect, transform and analyze SpaceX launches data.
1. API communication is performed using client generated from **OpenApiV3** schema (supplied with this project).
2. Metric collection is implemented in a form Prometheus compliant collector, calling an external API on the one hand and exposing results in **OpenMetrics** format.
3. Additionally CSV exporter is available, allowing to download a csv file for any metric collected by this project.
4. Metrics analysis and visualization is performed using Pandas dataframes and Bokeh dashboard. 
5. Optionally, one can pull data from **/api/prom/metrics** directly into Prometheus server instance for later analysis and visualization.
6. API calls performed by collector are cached to reduce remote server load and improve responsiveness.

### Prerequisites
- Docker
- openapi-generator (optional)

### Running
```
docker run --rm -v $(pwd):/app -w /app -p 8050:8050 -it $(docker build -q .) python app.py
```

### Endpoints
| Endpoint | Location |
| -------- | -------- |
| **Dashboard** | **localhost:8050** |
| List of available metrics | localhost:8050/api/metrics |
| Fetch CSV of a given metric | localhost:8050/api/csv/<metric> |
| All metrics in Prometheus Text Format | localhost:8050/api/prom/metrics |
