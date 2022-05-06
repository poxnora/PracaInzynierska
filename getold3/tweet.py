import snscrape.modules.twitter as sntwitter
import pandas as pd
maxTweets = 200
tweets_list = []


def getTweets():

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(PKO OR #PKO OR $PKO) AND -PKOEKSTRAKLASA AND -(PKO Ekstraklasa) AND -#PKOEkstraklasa AND -PKOEKSTRAKLASY AND -(Ekstraklasy) AND -#Ekstraklasy AND -PKOEKSTRAKLASIE AND -(Ekstraklasie) AND -#Ekstraklasie lang:pl -is:retweet').get_items()):
        if i>maxTweets:
            break
        tweets_list.append([ tweet.id,tweet.date,tweet.retweetCount, tweet.likeCount, tweet.content])


    tweets_df2 = pd.DataFrame(tweets_list, columns=['Tweet Id','Datetime','retweetCount','likeCount', 'Text' ])
    tweets_df2.to_csv('PKOst.csv', sep=';', index=False)


