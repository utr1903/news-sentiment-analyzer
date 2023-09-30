import os
import json
import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set variables
apikey = os.getenv("GNEWS_API_KEY")
language = "en"
country = "us"
numMaxNews = 10
search = "Microsoft"
url = f'https://gnews.io/api/v4/search?q={search}&lang={language}&country={country}&max={numMaxNews}&apikey={apikey}'

# Fetch news & analyze
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]

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
        sentimentAnalyzer = SentimentIntensityAnalyzer()
        sentimentScores = sentimentAnalyzer.polarity_scores(title)

        # Print sentiment scores
        compound = sentimentScores["compound"]
        neg = sentimentScores["neg"]
        neu = sentimentScores["neu"]
        pos = sentimentScores["pos"]

        print(f"compound: {compound} | neu: {neu} | pos: {pos} | neg: {neg}")
        print()
