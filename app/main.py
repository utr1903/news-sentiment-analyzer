from opentelemetry import trace
from opentelemetry.trace import SpanKind

from newsfetchers.gnews.gnews import Gnews
from nlpanalyzers.transformers.analyzer import TransformerAnalyzer
from otel.otel import init as initOtel


def analyzeGnews(
    analyzer,
    company,
):
    # Set variables
    language = "en"
    country = "us"
    numMaxNews = 10

    # Analyze Google News
    gnews = Gnews(analyzer)
    gnews.fetchAndAnalyzeArticles(
        language, country, numMaxNews, company)


def analyzeNewsOfCompanies(
    analyzer,
    companies,
):
    # Get the global tracer
    tracer = trace.get_tracer(__name__)

    # Loop over all companies
    for company in companies:

        # Start parent span for all news sources
        with tracer.start_as_current_span(company, kind=SpanKind.SERVER):
            analyzeGnews(analyzer, company)


def main():

    # Instantiate Open Telemetry SDK
    initOtel()

    # Instantiate sentiment analyzer
    analyzer = TransformerAnalyzer()

    # Hardcoded company list (currently)
    companies = [
        "Microsoft",
    ]

    # Fetch news of companies and analyze their sentiments
    analyzeNewsOfCompanies(analyzer, companies)


main()
