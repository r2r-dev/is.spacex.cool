### Building
```sh
docker build . -t spacex:latest
```

### Running
```
docker run -v $(pwd):/app -w /app -p 8050:8050 -it spacex:latest python app.py
```

### Endpoints
| Endpoint | Location |
| -------- | -------- |
| Dashboard | localhost:8050 |
| List of available metrics | localhost:8050/api/metrics |
| Fetch CSV of a given metric | localhost:8050/api/csv/<metric> |
| All metrics in Prometheus Text Format | localhost:8050/api/prom/metrics |
