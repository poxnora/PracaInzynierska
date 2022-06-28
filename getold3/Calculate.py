import pandas as pd


class Calculate:

    def __init__(self, doc, n):
        self.doc = doc
        self.doc_time = doc
        self.doc_time['Datetime'] = pd.to_datetime(self.doc['Datetime'], errors='coerce')
        self.dates = doc['Datetime'].dt.strftime('%Y-%m-%d')
        self.doc_time['Datetime'] = self.dates
        self.dates_set = (x for x in self.dates)
        self.n = n

    def retweet_top(self):
        return self.doc.nlargest(n=self.n, columns=['retweetCount'])['Tweet Id']

    def likes_top(self):
        return self.doc.nlargest(n=self.n, columns=['likeCount']).index.values

    def most_positive_top(self):
        return self.doc.nlargest(n=self.n, columns=['Label']).index.values

    def most_negative_top(self):
        return self.doc.nsmallest(n=self.n, columns=['Label']).index.values

    def each_day_number(self):
        value_map = {}
        for date in self.dates:
            value = value_map.get(date)
            if value is None:
                value_map.update({date: 1})
            else:
                value += 1
                value_map.update({date: value})
        return value_map

    def each_day_sentiment_mean(self):
        value_map = {}
        for date in self.dates_set:
            r = self.doc_time[self.doc_time['Datetime'] == date]
            mean = r['Label'].mean()
            if mean != 0:
                value_map.update({date: mean})
        return value_map

    def last_n_sentiment_mean(self,n):
        ranges = 0
        mean = []
        true_mean = 0
        for date in self.dates_set:
            ranges += 1
            if ranges < n:
                r = self.doc_time[self.doc_time['Datetime'] == date]
                mean.append(r['Label'].mean())
            else:
                break
        for number in mean:
            true_mean += number
        return true_mean / len(mean)

    def all_positive_number(self):
        number = 0
        for sentiment in self.doc['Label']:
            if float(sentiment) > 0.3:
                number += 1
        return number

    def all_negative_number(self):
        number = 0
        for sentiment in self.doc['Label']:
            if float(sentiment) < -0.3:
                number += 1
        return number

