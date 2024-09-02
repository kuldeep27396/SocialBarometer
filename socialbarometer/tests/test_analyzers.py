from socialbarometer.analyzers.sentiment_analyzer import SentimentAnalyzer


def test_sentiment_analyzer():
    analyzer = SentimentAnalyzer()

    positive_result = analyzer.analyze("I love this product!")
    assert positive_result[0] == 'positive'
    assert positive_result[1] > 0

    negative_result = analyzer.analyze("I hate this product!")
    assert negative_result[0] == 'negative'
    assert negative_result[1] < 0

    neutral_result = analyzer.analyze("This product exists.")
    assert neutral_result[0] == 'neutral'
    assert -0.1 <= neutral_result[1] <= 0.1