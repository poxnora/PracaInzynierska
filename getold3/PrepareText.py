import re
import pandas as pd
import spacy
import unidecode
from gensim.models import Phrases
from gensim.models.phrases import Phraser


# noinspection DuplicatedCode
class PrepareText:
    # TODO implement for all files
    nlp = spacy.load("pl_core_news_md")
    col_list = ['Tweet Id', 'Datetime', 'retweetCount', 'likeCount', 'Text']
    pd.options.mode.chained_assignment = None
    doc = ""
    name = ""

    def __init__(self,doc):
        self.doc = doc


    def copy(self):
        self.doc.to_csv('tweets/PKOstcopy.csv', sep=';', index=False)
        copycsv = pd.read_csv('tweets/PKOstcopy.csv', delimiter=';', usecols=self.col_list)
        return copycsv

    def lemmatization(self):
        a = 0
        for line in self.doc['Text']:
            rep = line
            for token in self.nlp(str(line)):
                rep = str(rep).replace(token.text, token.lemma_)
            self.doc['Text'][a] = rep
            a += 1
        return self.doc

    def remove_stop_words(self):
        stop_words = open("data/polish.stopwords.txt", "r", encoding='utf-8')
        counter = 0
        for line in self.doc['Text']:
            line_copy = line
            list_words = list(line_copy.split(" "))
            rep = list_words
            for words in stop_words:
                stop_word = words.strip("\n")
                if stop_word in list_words:
                    rep.remove(stop_word)
            stop_words.seek(0)
            self.doc['Text'][counter] = " ".join(rep)
            counter += 1
        stop_words.close()
        return self.doc

    def clean_special(self):
        counter = 0
        for line in self.doc['Text']:
            line_clean_html = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", str(line))
            line_clean_men = re.sub("@[A-Za-z0-9_]+", " ", str(line_clean_html))
            line_clean_hash = re.sub("#[A-Za-z0-9_]+", " ", str(line_clean_men))
            line_clean = re.sub("[^A-Za-złąśćężóń]+", ' ', str(line_clean_hash)).lower()
            line_clean_short = re.sub(r'\W*\b\w{1,2}\b', '', str(line_clean))
            line_clean_special = unidecode.unidecode(line_clean_short, "utf-8")
            self.doc['Text'][counter] = unidecode.unidecode(line_clean_special)
            counter += 1
        return self.doc

    def clean_special_without_polish(self):
        counter = 0
        for line in self.doc['Text']:
            line_clean_html = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", str(line))
            line_clean_men = re.sub("@[A-Za-z0-9_]+", " ", str(line_clean_html))
            line_clean_hash = re.sub("#[A-Za-z0-9_]+", " ", str(line_clean_men))
            line_clean = re.sub("[^A-Za-złąśćężóń]+", ' ', str(line_clean_hash)).lower()
            line_clean_short = re.sub(r'\W*\b\w{1,2}\b', '', str(line_clean))
            self.doc['Text'][counter] = line_clean_short
            counter += 1
        return self.doc

    def bigrams(self):
        tab = []
        counter = 0
        for line in self.doc['Text']:
            tab.append(line.split())
        phrases = Phrases(tab, min_count=7, progress_per=10000)
        bigram = Phraser(phrases)
        sentences = bigram[tab]
        for line in sentences:
            self.doc['Text'][counter] = " ".join(line)
            counter += 1
        return self.doc
