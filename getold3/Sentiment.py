from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
col_list = ['Tweet Id','Datetime','retweetCount','likeCount', 'Text']


class Sentiment:

    def __init__(self,doc):
        self.doc = doc

    def get_sentiment(self):
        label = []
        analyzer = SentimentIntensityAnalyzer()
        for line in self.doc['Text']:
            dictionary = analyzer.polarity_scores(line)
            sentiment = dictionary["pos"] - dictionary["neg"]
            label.append(sentiment)
        self.doc['Label'] = label
        return self.doc

        """analyzer.polarity_scores("zly")
        print(analyzer.polarity_scores("zly"))
        print(analyzer.polarity_scores("zły"))
        print(analyzer.polarity_scores("zniechęcić"))
        print(analyzer.polarity_scores("zniechecic"))"""