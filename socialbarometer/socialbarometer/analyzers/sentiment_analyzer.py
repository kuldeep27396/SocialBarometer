from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0.1:
            return 'positive', sentiment
        elif sentiment < -0.1:
            return 'negative', sentiment
        else:
            return 'neutral', sentiment