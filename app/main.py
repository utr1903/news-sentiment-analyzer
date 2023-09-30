from nltk.sentiment.vader import SentimentIntensityAnalyzer
from gnews.gnews import Gnews

# Set variables
language = "en"
country = "us"
numMaxNews = 10
search = "Microsoft"

# Fetch Google News
gnews = Gnews()
articles = gnews.fetchNews(language, country, numMaxNews, search)

# Analyze news
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
    sentimentAnalyzer = SentimentIntensityAnalyzer()
    sentimentScores = sentimentAnalyzer.polarity_scores(title)

    # Print sentiment scores
    compound = sentimentScores["compound"]
    neg = sentimentScores["neg"]
    neu = sentimentScores["neu"]
    pos = sentimentScores["pos"]

    print(f"compound: {compound} | neu: {neu} | pos: {pos} | neg: {neg}")
    print()

print("Google news are analyzed successfully.")
