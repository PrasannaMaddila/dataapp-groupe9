import matplotlib.pyplot as plt
import pandas as pd
from difflib import *
from pytest import *
import json

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]

# returns a dictionnay
# keys: Misses names, values : pair of (positive,negative)
def misses_opinions(df=corpus_dataframe):
    dict = {}
    for ann in df['annotations']:
        ann = json.loads(ann.replace("'", '"'))
        for topic in ann['topics']:
            words = topic['name'].lower().split()
            if words[0] == 'miss':
                if not topic['name'].upper() in dict:
                    dict[topic['name'].upper()] = (0,0)
                (a,b) = dict[topic['name'].upper()]
                if topic['opinion'] == 'positive':
                    a += 1
                else: b += 1
                dict[topic['name'].upper()] = (a,b)
    return dict

def pie_chart(df):
    raise NotImplementedError


def histogram_miss_tweet_number(df):
    raise NotImplementedError


def miss_pos_neg_data(df):
    raise NotImplementedError

print(misses_opinions())
