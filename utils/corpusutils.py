import numpy as np
import pandas as pd
from pytest import *


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


def test_load_tweet_with_annotation():
    id = "143048389142134785"
    dict = load_tweet_with_annotation(id)
    assert dict = {'id': "143048389142134785", 'text': "Ce soir c'est l'élection de #missfrance et je vais me faire un plaisir de NE PAS regarder.", 'annotation': {'topics': [{'name': 'Languedoc', 'opinion': 'positive'}, {'name': 'Nord-Pas-De-Calais', 'opinicon': 'negative'}], 'negative_keywords': ['pas aime'], 'positive_keywords': ['jolie', 'aime']}}
    id = "143049242305495040"
    dict = load_tweet_with_annotation(id)
    assert dict = "No annotations"


def load_corpus_in_dataframe():
    ids = open(tweetdir+'tweets-ids').readlines()
    dict = {}
    for id in ids:
        dict[id] = load_tweet_with_annotation(id)
    return pd.DataFrame.from_dict(dict)
