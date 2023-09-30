import os
import json
import urllib.request


class Gnews:
    def __init__(self):
        self.apiKey = os.getenv("GNEWS_API_KEY")

    def fetchNews(
        self,
        language,
        country,
        numMaxNews,
        search
    ):
        print("Fetching Google news...")
        # Prepare URL with parameters
        url = f'https://gnews.io/api/v4/search?q={search}&lang={language}&country={country}&max={numMaxNews}&apikey={self.apiKey}'

        # Fetch news
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode("utf-8"))
                articles = data["articles"]

                print("Google news are fetched successfully.")

                return articles
        except Exception as e:
            print(f"Unexpected error is occurred: {e}")
