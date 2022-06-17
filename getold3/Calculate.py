import pandas as pd


class Calculate:
    doc = ""
    n = 0

    def __init__(self, doc, n):
        self.doc = doc
        self.n = n

    def retweet(self):
        return self.doc.nlargest(n=self.n, columns=['retweetCount'])['Tweet Id']

    def likes(self):
        return self.doc.nlargest(n=self.n, columns=['likeCount']).index.values

    def most_positive(self):
        return self.doc.nlargest(n=self.n, columns=['Label']).index.values

    def most_negative(self):
        return self.doc.nsmallest(n=self.n, columns=['Label']).index.values

    def each_day(self):
        self.doc['Datetime'] = pd.to_datetime(self.doc['Datetime'], errors='coerce')
        dates = self.doc['Datetime'].dt.strftime('%Y-%m-%d')
        value_map = {}
        for date in dates:
            value = value_map.get(date)
            if value is None:
                value_map.update({date: 1})
            else:
                value += 1
                value_map.update({date: value})
        print(value_map)
        return value_map

    def each_day_sentiment(self):
        self.doc['Datetime'] = pd.to_datetime(self.doc['Datetime'], errors='coerce')
        dates = self.doc['Datetime'].dt.strftime('%Y-%m-%d')
        self.doc['Datetime'] = dates
        value_map = {}
        dates_set = (x for x in dates)
        for date in dates_set:
            r = self.doc[self.doc['Datetime'] == date]
            mean = r['Label'].mean()
            if mean != 0:
                value_map.update({date: mean})
        return value_map
