# News Sentiment Analyzer

This repo is dedicated to fetch news for various topics and analyze them according to natural language processing algorithms.

In order to run the app locally, first install the dependencies:

```shell
cd ./app
pip3 install -r "requirements.txt"
```

Then, run the [`main.py`](/app/main.py):

```shell

GNEWS_API_KEY="<YOUR_GNEWS_API_KEY>" OTEL_SERVICE_NAME="newsanalyzer" OTEL_EXPORTER_OTLP_ENDPOINT="<YOUR_OTLP_ENDPOINT>" OTEL_EXPORTER_OTLP_HEADERS="api-key=<OTLP_CREDENTIAL>" python3 main.py

```

For New Relic:

```shell
GNEWS_API_KEY="<YOUR_GNEWS_API_KEY>" OTEL_SERVICE_NAME="newsanalyzer" OTEL_EXPORTER_OTLP_ENDPOINT="<NEWRELIC_OTLP_ENDPOINT>" OTEL_EXPORTER_OTLP_HEADERS="api-key=<NEWRELIC_LICENSE_KEY>" python3 main.py

```

where the New Relic endpoint is

- `https://otlp.nr-data.net:4317` for `US`
- `https://otlp.eu01.nr-data.net:4317` for `EU`
