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
        # Fetch articles
        articles = self.__fetchArticles(
            language,
            country,
            numMaxNews,
            search,
        )

        # Analyze articles
        self.__analyzeArticles(articles)

    def __fetchArticles(
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

        # Fetch news
        print("Fetching Google news...")
        articles = []

        with tracer.start_as_current_span("Gnews", kind=SpanKind.CLIENT) as span:
            try:
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    articles = data["articles"]

                print("Google news are fetched successfully.")
                return articles

            except Exception as e:
                print(f"Unexpected error is occurred: {e}")
                span.set_status(StatusCode.ERROR)
                span.record_exception(e, escaped=True)

    def __analyzeArticles(
        self,
        articles,
    ):
        print("Analyzing Google news...")

        # Get the global tracer
        tracer = trace.get_tracer(__name__)

        for articleCounter in range(len(articles)):

            # Extract article info
            title = articles[articleCounter]['title']
            description = articles[articleCounter]['description']
            url = articles[articleCounter]['url']
            publishedAt = articles[articleCounter]['publishedAt']

            try:
                # Create separate span for each sentiment analysis
                with tracer.start_as_current_span(title, kind=SpanKind.INTERNAL) as span:

                    # Calculate sentiment
                    sentiment = self.analyzer.analyzeStatement(title)

                    # Set span attributes
                    span.set_attribute("news.title", title)
                    span.set_attribute("news.description", description)
                    span.set_attribute("news.url", url)
                    span.set_attribute("news.publishedAt", publishedAt)
                    span.set_attribute("news.sentiment", sentiment)

            except Exception as e:
                print(f"Unexpected error is occurred: {e}")
                span.set_status(StatusCode.ERROR)
                span.record_exception(e, escaped=True)

        print("Google news are analyzed successfully.")
