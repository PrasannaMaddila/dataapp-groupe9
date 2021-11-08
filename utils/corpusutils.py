import numpy as np
import pandas as pd

datadir = '../Data/'
annodir = datadir+'/tweets-annotations/'
tweetdir = datadir+'/tweets/'

def read_and_load_ann_annotation(filename):


def load_tweet_with_annotation(id):
    S = read_and_load_ann_annotation(annodir+id+'.ann')
    if S == {}:
        return("No annotations")
    else:
        res = {}
        res['id'] = id
        res['text'] = open(tweetdir+id+'.txt').read()
        res['annotations'] = S
        return(res)


def load_corpus_in_dataframe():
    ids = open(tweetdir+'tweets-ids').readlines()
    dict = {}
    for id in ids:
        dict[id] = load_tweet_with_annotation(id)
    return pd.DataFrame.from_dict(dict)
