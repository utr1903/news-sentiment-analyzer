from newsfetchers.gnews.gnews import Gnews
from nlpanalyzers.transformers.analyzer import TransformerAnalyzer

# Instantiate sentiment analyzer
analyzer = TransformerAnalyzer()

# Set variables
language = "en"
country = "us"
numMaxNews = 10
search = "Microsoft"

# Analyze Google News
gnews = Gnews(analyzer)
gnews.fetchAndAnalyzeArticles(language, country, numMaxNews, search)
