# import numpy as np
import pandas as pd
from ast import literal_eval
from pytest import *

""" my_string = "{'key':'val','key2':2}"
my_dict = ast.literal_eval(my_string)

 """


corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
# Drops the automatically added index column
corpus_dataframe = corpus_dataframe.iloc[:, 1:]
# Re-converts the string dictionary to the dictionary-dictionary
corpus_dataframe = corpus_dataframe.assign(
    annotations=literal_eval(corpus_dataframe["annotations"])
)
print(corpus_dataframe["annotations"][:]["topics"])


def nb_tweets():
    return corpus_dataframe


def nb_annotations():
    return 1


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


def size_negative_vocab():
    return 1


# print("Num. of subjects: " + nb_subjects() + "\n")
# print("Subjects: \n" + subjects)
