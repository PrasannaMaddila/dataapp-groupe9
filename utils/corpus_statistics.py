# import numpy as np
import pandas as pd
import json
from pytest import *

# from corpusutils import corpus_dataframe

""" my_string = "{'key':'val','key2':2}"
my_dict = ast.literal_eval(my_string)

 """


corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
# Drops the automatically added index column
corpus_dataframe = corpus_dataframe.iloc[:, 1:]
# Re-converts the string dictionary to the dictionary-dictionary
""" for ann in corpus_dataframe["annotations"]:
    ann_dict = json.loads(ann.replace("'", '"'))
print(type(corpus_dataframe["annotations"][0])) """


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
    return 1


def nb_negative_opinions():
    return 1


def size_positive_vocab():
    return 1


# Need to update for using literal_eval'ed dataframe
def size_negative_vocab():
    negative_keywords = set()
    for ann in corpus_dataframe["annotations"]:
        ann_dict = json.loads(ann.replace("'", '"'))
        negative_keywords |= set(ann_dict["negative_keywords"])
    print(negative_keywords)
    return len(negative_keywords)


print(nb_tweets(), nb_annotations())
print(size_negative_vocab())
print(nb_subjects(corpus_dataframe), subjects(corpus_dataframe))
