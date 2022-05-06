import re
import pandas as pd
from time import time
from collections import defaultdict
import spacy
import logging
import pyMorfologik
import unidecode

nlp = spacy.load("pl_core_news_md")
pd.options.mode.chained_assignment = None
col_list = ['Tweet Id','Datetime','retweetCount','likeCount', 'Text']

def copy(doc):
    doc.to_csv('PKOstcopy.csv', sep=';', index=False)
    copycsv = pd.read_csv('PKOstcopy.csv', delimiter=';', usecols=col_list)
    return copycsv


def lemmatization(doc):
    a = 0
    for line in doc['Text']:
        rep = line
        for token in nlp(str(line)):
            rep = str(rep).replace(token.text, token.lemma_)
        doc['Text'][a] = rep
        a += 1
    return doc


def remove_stop_words(doc):
    stop_words = open("polish.stopwords.txt", "r", encoding='utf-8')
    a = 0
    for line in doc['Text']:
        line_copy = line
        list_words = list(line_copy.split(" "))
        rep = list_words
        for words in stop_words:
            stop_word = words.strip("\n")
            if stop_word in list_words:
                rep.remove(stop_word)
        stop_words.seek(0)
        doc['Text'][a] = " ".join(rep)
        a += 1
    stop_words.close()
    return doc


def clean_special(doc):
    a = 0
    for line in doc['Text']:
        line_clean_html = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", str(line))
        line_clean_men = re.sub("@[A-Za-z0-9_]+", " ", str(line_clean_html))
        line_clean_hash = re.sub("#[A-Za-z0-9_]+", " ", str(line_clean_men))
        line_clean = re.sub("[^A-Za-złąśćężóń]+", ' ', str(line_clean_hash)).lower()
        line_clean_short = re.sub(r'\W*\b\w{1,1}\b', '', str(line_clean))
        line_clean_special = unidecode.unidecode(line_clean_short, "utf-8")
        doc['Text'][a] = unidecode.unidecode(line_clean_special)
        a += 1
    return doc
