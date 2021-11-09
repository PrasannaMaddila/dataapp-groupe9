# import numpy as np
import pandas as pd
import json
from pytest import *


corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
# Drops the automatically added index column
corpus_dataframe = corpus_dataframe.iloc[:, 1:]


def nb_tweets():
    return len(open('../Data/tweets-ids').readlines())

def nb_annotations():
    return len(corpus_dataframe['annotations'])


def nb_subjects():
    return len(corpus_dataframe["annotations"][:]["topics"])


def subjects():
    return corpus_dataframe["annotations"][1:]["topics"]


def nb_positive_opinions():
    return 1


def nb_negative_opinions():
    return 1


def size_positive_vocab():
    return 1


# Need to update for using literal_eval'ed dataframe
def size_negative_vocab():
    negative_keywords = set()
    for ann in corpus_dataframe['annotations']:
        ann_dict = json.loads(ann.replace("'", '"'))
        negative_keywords |= set(ann_dict['negative_keywords'])
    print(negative_keywords)
    return len(negative_keywords)

print(nb_tweets(), nb_annotations())
print(size_negative_vocab())
