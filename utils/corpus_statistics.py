# import numpy as np
import pandas as pd
from pytest import *
import json

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]


def nb_tweets():
    return len(open("../Data/tweets-ids").readlines())


def nb_annotations(df=corpus_dataframe):
    return len(df["annotations"])


def nb_subjects(df=corpus_dataframe):
    # return [ann_dict["topics"] for ann_dict in len(corpus_dataframe["annotations"])
    return len(subjects(df))


def subjects(df=corpus_dataframe):
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
            for topic in ann_dict["topics"]:
                subs.append(topic["name"])
        except:
            # Else, Do nothing
            continue
    return subs


def nb_positive_opinions(df=corpus_dataframe):
    res = 0
    for i in df["annotations"]:
        dict_ann = json.loads(i.replace("'", '"'))
        topics = dict_ann["topics"]
        for k in topics:
            if k["opinion"] == "positive":
                res += 1
    return res


def nb_negative_opinions(df=corpus_dataframe):
    res = 0
    for i in df["annotations"]:
        dict_ann = json.loads(i.replace("'", '"'))
        topics = dict_ann["topics"]
        for k in topics:
            if k["opinion"] == "negative":
                res += 1
    return res


def size_positive_vocab(df=corpus_dataframe):
    res = set()
    for i in df["annotations"]:
        dict_ann = json.loads(i.replace("'", '"'))
        res |= set(dict_ann["positive_keywords"])
    return len(res)


def size_negative_vocab(df=corpus_dataframe):
    negative_keywords = set()
    for ann in df["annotations"]:
        ann_dict = json.loads(ann.replace("'", '"'))
        negative_keywords |= set(ann_dict["negative_keywords"])
    return len(negative_keywords)

# print(nb_tweets())
# print(nb_annotations())
# print(nb_negative_opinions())
# print(nb_positive_opinions())
print(nb_subjects())
print(subjects())
# print(size_positive_vocab())
# print(size_negative_vocab())