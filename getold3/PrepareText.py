import re
import pandas as pd
import spacy
import unidecode
from gensim.models import Phrases
from gensim.models.phrases import Phraser


class PrepareText:
    # TODO implement for all files
    col_list = ['Tweet Id', 'Datetime', 'retweetCount', 'likeCount', 'Text']
    pd.options.mode.chained_assignment = None

    def __init__(self,doc):
        self.doc = doc
        self.nlp = spacy.load("pl_core_news_md")

    def copy(self):
        self.doc.to_csv('tweets/PKOstcopy.csv', sep=';', index=False)
        copy_csv = pd.read_csv('tweets/PKOstcopy.csv', delimiter=';', usecols=self.col_list)
        return copy_csv

    def lemmatization(self):
        index = 0
        for line in self.doc['Text']:
            line = self.nlp(line)
            self.doc['Text'][index] = (" ".join([token.lemma_ for token in line]))
        return self.doc

    def remove_stop_words(self):
        stop_words = open("data/polish.stopwords.txt", "r", encoding='utf-8')
        index = 0
        for line in self.doc['Text']:
            line_copy = line
            list_words = list(line_copy.split(" "))
            rep = list_words
            for words in stop_words:
                stop_word = words.strip("\n")
                if stop_word in list_words:
                    rep.remove(stop_word)
            stop_words.seek(0)
            self.doc['Text'][index] = " ".join(rep)
            index += 1
        stop_words.close()
        return self.doc

    def clean_special(self):
        index = 0
        for line in self.doc['Text']:
            line_clean_html = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", str(line))
            line_clean_men = re.sub("@[A-Za-z0-9_]+", " ", str(line_clean_html))
            line_clean_hash = re.sub("#[A-Za-z0-9_]+", " ", str(line_clean_men))
            line_clean = re.sub("[^A-Za-złąśćężóń]+", ' ', str(line_clean_hash)).lower()
            line_clean_short = re.sub(r'\W*\b\w{1,2}\b', '', str(line_clean))
            line_clean_special = unidecode.unidecode(line_clean_short, "utf-8")
            self.doc['Text'][index] = unidecode.unidecode(line_clean_special)
            index += 1
        return self.doc

    def clean_special_without_polish(self):
        index = 0
        for line in self.doc['Text']:
            line_clean_html = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", str(line))
            line_clean_men = re.sub("@[A-Za-z0-9_]+", " ", str(line_clean_html))
            line_clean_hash = re.sub("#[A-Za-z0-9_]+", " ", str(line_clean_men))
            line_clean = re.sub("[^A-Za-złąśćężóń]+", ' ', str(line_clean_hash)).lower()
            line_clean_short = re.sub(r'\W*\b\w{1,2}\b', '', str(line_clean))
            self.doc['Text'][index] = line_clean_short
            index += 1
        return self.doc

    def bigrams(self):
        tab = []
        index = 0
        for line in self.doc['Text']:
            tab.append(line.split())
        phrases = Phrases(tab, min_count=7, progress_per=10000)
        bigram = Phraser(phrases)
        sentences = bigram[tab]
        for line in sentences:
            self.doc['Text'][index] = " ".join(line)
            index += 1
        return self.doc

    def prepare(self):
        self.doc = self.clean_special_without_polish()
        self.doc = self.lemmatization()
        self.doc = self.remove_stop_words()
        return self.doc
