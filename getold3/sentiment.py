import pandas as pd
from gensim.models.phrases import Phrases, Phraser
import multiprocessing
from gensim.models import Word2Vec

col_list = ['Tweet Id','Datetime','retweetCount','likeCount', 'Text']

def bigrams(doc):
    tab = []
    a = 0
    for line in doc['Text']:
        tab.append(line.split())
    phrases = Phrases(tab, min_count=1, progress_per=10000)
    bigram = Phraser(phrases)
    sentences = bigram[tab]
    doc.to_csv('PKOstcopysentences.csv', sep=';', index=False)
    sentences_csv = pd.read_csv('PKOstcopysentences.csv', delimiter=';', usecols=col_list)
    for line in bigram[tab]:
        sentences_csv['Text'][a] = line
        a += 1
    return sentences


def w2v(doc,sentences):
    w2v_model = Word2Vec(min_count=20,
                         window=2,
                         sample=6e-5,
                         alpha=0.03,
                         min_alpha=0.0007,
                         negative=20,
                         workers=6 - 1)
    w2v_model.build_vocab(sentences, progress_per=10000)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    w2v_model.wv.most_similar(positive=["pko"])