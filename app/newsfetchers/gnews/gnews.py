import os
import json
import urllib.request

from opentelemetry import trace
from opentelemetry.trace import StatusCode, SpanKind


class Gnews:
    def __init__(
        self,
        analyzer,
    ):
        self.apiKey = os.getenv("GNEWS_API_KEY")
        self.analyzer = analyzer

    def fetchAndAnalyzeArticles(
        self,
        language,
        country,
        numMaxNews,
        search
    ):
        # Prepare URL with parameters
        url = f'https://gnews.io/api/v4/search?q={search}&lang={language}&country={country}&max={numMaxNews}&apikey={self.apiKey}'

        # Get the global tracer
        tracer = trace.get_tracer(__name__)
        try:
            # Fetch news
            print("Fetching Google news...")
            articles = []

            with tracer.start_as_current_span("Gnews", kind=SpanKind.CLIENT) as span:
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    articles = data["articles"]

            print("Google news are fetched successfully.")

            print("Analyzing Google news...")
            for articleCounter in range(len(articles)):

                # Extract information
                title = articles[articleCounter]['title']
                description = articles[articleCounter]['description']
                url = articles[articleCounter]['url']
                publishedAt = articles[articleCounter]['publishedAt']
                sentiment = self.analyzer.analyzeStatement(title)

                # Create separate span for each sentiment analysis
                with tracer.start_as_current_span(title, kind=SpanKind.INTERNAL) as span:
                    span.set_attribute("news.title", title)
                    span.set_attribute("news.description", description)
                    span.set_attribute("news.url", url)
                    span.set_attribute("news.publishedAt", publishedAt)
                    span.set_attribute("news.sentiment", sentiment)

                print("Google news are analyzed successfully.")

        except Exception as e:
            print(f"Unexpected error is occurred: {e}")
            span.set_status(StatusCode.ERROR)
            span.record_exception(e, escaped=True)
