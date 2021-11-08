import numpy as np
import pandas as pd


def read_and_load_ann_annotation(filename):


def load_tweet_with_annotation(id):
    S = read_and_load_ann_annotation(id+'.ann')
    if S == {}:
        return("No annotations")
    else:
        res = {}
        res['id'] = id
        res['text'] = open(id+'.txt').read()
        res['annotations'] = S
        return(res)


def load_corpus_in_dataframe():
