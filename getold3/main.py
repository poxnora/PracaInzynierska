import logging
import pandas as pd

from Calculate import Calculate
from Plots import Plots
from Sentiment import Sentiment
from getold3.PrepareText import PrepareText

logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
col_list1 = ['Tweet Id','Datetime','retweetCount','likeCount', 'Text','Label']
col_list = ['Tweet Id','Datetime','retweetCount','likeCount', 'Text']
#TODO implement choosing files
"""
csv = pd.read_csv('tweets/PKOst.csv', delimiter=';', usecols=col_list)
copy = prepare_text.copy(csv)
prepare_text.lemmatization(copy).to_csv('tweets/PKOstcopy.csv', sep=';', index=False)
copy_lem = pd.read_csv('tweets/PKOstcopy.csv', delimiter=';', usecols=col_list)
prepare_text.clean_special(copy_lem).to_csv('tweets/PKOstcopy.csv', sep=';', index=False)
copy_lem_special = pd.read_csv('tweets/PKOstcopy.csv', delimiter=';', usecols=col_list)
prepare_text.remove_stop_words(copy_lem_special).to_csv('tweets/PKOstcopy.csv', sep=';', index=False)
copy_clean = pd.read_csv('tweets/PKOstcopy.csv', delimiter=';', usecols=col_list)
prepare_text.bigrams(copy_clean).to_csv('tweets/PKOstcopysentences.csv', sep=';', index=False)
sentiment = Sentiment(copy_clean)
sentiment.get_sentiment().to_csv('tweets/PKOstcopysentencespol.csv', sep=';', index=False)

copy_clean = pd.read_csv('tweets/PKOstcopysentencespol.csv', delimiter=';', usecols=col_list)
calculator = Calculate(copy_clean,5)
plots = Plots()
plots.popularity_plot(calculator.each_day())
"""
csv = pd.read_csv('tweets/PKO.csv', delimiter=';', usecols=col_list)
prepare = PrepareText(csv)
prepare.prepare().to_csv('tweets/PKOclean.csv', sep=';', index=False)

