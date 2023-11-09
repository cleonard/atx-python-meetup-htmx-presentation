from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()


def sentiment(text):
    values = sid.polarity_scores(text)
    return values
