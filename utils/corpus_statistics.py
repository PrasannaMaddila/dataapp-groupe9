# import numpy as np
import pandas as pd
from pytest import *
import json

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]


def nb_tweets():
    return len(open("../Data/tweets-ids").readlines())


def nb_annotations():
    return len(corpus_dataframe["annotations"])


def nb_subjects(df):
    # return [ann_dict["topics"] for ann_dict in len(corpus_dataframe["annotations"])
    return len(subjects(df))


def subjects(df):
    subs = []
    for ann in df["annotations"]:
        ann_dict = json.loads(ann.replace("'", '"'))
        # print((ann_dict["topics"][0]["name"]))
        # Case: Topics could be empty
        try:
            # If it works it works,
            # Note: JSON returns a list of dictionary
            # of size 1, i.e. it contains only our dict.
            # Hence, the extra [0]
            subs.append(ann_dict["topics"][0]["name"])
        except:
            # Else, Do nothing
            continue
    return subs


def nb_positive_opinions():
    res = 0
    for i in corpus_dataframe["annotations"]:
        dict_ann = json.loads(i.replace("'", '"'))
        topics = dict_ann["topics"]
        for k in topics:
            if k["opinion"] == "positive":
                res += 1
    return res


def nb_negative_opinions():
    res = 0
    for i in corpus_dataframe["annotations"]:
        dict_ann = json.loads(i.replace("'", '"'))
        topics = dict_ann["topics"]
        for k in topics:
            if k["opinion"] == "negative":
                res += 1
    return res


def size_positive_vocab():
    res = {}
    for i in corpus_dataframe["annotations"]:
        dict_ann = json.loads(i.replace("'", '"'))
        res |= set(dict_ann["positive_keywords"])
    return res


def size_negative_vocab():
    negative_keywords = set()
    for ann in corpus_dataframe["annotations"]:
        ann_dict = json.loads(ann.replace("'", '"'))
        negative_keywords |= set(ann_dict["negative_keywords"])
    return len(negative_keywords)
