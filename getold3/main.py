import logging

import pandas as pd


import cleantext
import sentiment
import tweet


logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)



col_list = ['Tweet Id','Datetime','retweetCount','likeCount', 'Text']
csv = pd.read_csv('PKOst.csv', delimiter=';', usecols=col_list)
"""
copy = cleantext.copy(csv)
cleantext.lemmatization(copy).to_csv('PKOstcopy.csv', sep=';', index=False)
copy_lem = pd.read_csv('PKOstcopy.csv', delimiter=';', usecols=col_list)
cleantext.clean_special(copy_lem).to_csv('PKOstcopy.csv', sep=';', index=False)
copy_lem_special = pd.read_csv('PKOstcopy.csv', delimiter=';', usecols=col_list)
cleantext.remove_stop_words(copy_lem_special).to_csv('PKOstcopy.csv', sep=';', index=False)
"""
copy_clean = pd.read_csv('PKOstcopy.csv', delimiter=';', usecols=col_list)

sentiment.bigrams(copy_clean)

