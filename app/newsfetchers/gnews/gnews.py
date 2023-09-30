import os
import json
import urllib.request


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

        try:
            # Fetch news
            print("Fetching Google news...")
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode("utf-8"))
                articles = data["articles"]

                print("Google news are fetched successfully.")

                print("Analyzing Google news...")
                for articleCounter in range(len(articles)):

                    # title
                    title = articles[articleCounter]['title']
                    print(f"title: {title}")

                    # description
                    description = articles[articleCounter]['description']
                    print(f"description: {description}")

                    # url
                    url = articles[articleCounter]['url']
                    print(f"url: {url}")

                    # publishedAt
                    publishedAt = articles[articleCounter]['publishedAt']
                    print(f"publishedAt: {publishedAt}")

                    # sourceName
                    sourceName = articles[articleCounter]['source']['name']
                    print(f"source.name: {sourceName}")

                    # sourceUrl
                    sourceUrl = articles[articleCounter]['source']['url']
                    print(f"source.url: {sourceUrl}")

                    # Analyze sentiment
                    sentiment = self.analyzer.analyzeStatement(title)
                    print(f"sentiment: {sentiment}")

                print("Google news are analyzed successfully.")

        except Exception as e:
            print(f"Unexpected error is occurred: {e}")
