# import numpy as np
import pandas as pd
from pytest import *
import json as json

from dataapp_groupe_9.utils.corpusutils import read_and_load_ann_annotation

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]


def nb_tweets():
    return 1


def nb_annotations():
    return 1


def nb_subjects():
    return 1


def subjects():
    return []


def nb_positive_opinions():
    res = 0
    for i in corpus_dataframe['annotations']:
        dict_ann = json.loads(i.replace("'", '"'))
        topics = dict_ann['topics']
        for k in topics:
            if k['opinion'] == 'positive':
                res += 1
    return res


def nb_negative_opinions():
    res = 0
    for i in corpus_dataframe['annotations']:
        dict_ann = json.loads(i.replace("'", '"'))
        topics = dict_ann['topics']
        for k in topics:
            if k['opinion'] == 'negative':
                res += 1
    return res


def size_positive_vocab():
    res = {}
    for i in corpus_dataframe['annotations']:
        dict_ann = json.loads(i.replace("'", '"'))
        res |= set(dict_ann['positive_keywords'])
    return(res)


def size_negative_vocab():
    return 1
