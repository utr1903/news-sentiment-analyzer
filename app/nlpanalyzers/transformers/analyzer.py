from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

from nlpanalyzers.analyzer import NlpAnalyzer


class TransformerAnalyzer(NlpAnalyzer):

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            'nlptown/bert-base-multilingual-uncased-sentiment')
        self.model = AutoModelForSequenceClassification.from_pretrained(
            'nlptown/bert-base-multilingual-uncased-sentiment')

    def analyzeStatement(
        self,
        statement,
    ):
        # Encode the statement in tokens
        tokens = self.tokenizer.encode(statement, return_tensors='pt')

        # Analyze sentiment
        result = self.model(tokens)

        # Calculate sentiment value
        sentiment = float(torch.argmax(result.logits)+1.0)

        return sentiment
