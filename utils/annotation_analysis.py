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
                close_keys = get_close_matches(topic['name'].lower(), dict.keys(), 1, 0.75)
                print(close_keys, topic['name'].lower())
                if close_keys:
                    close_keys = close_keys[0]
                    if len(topic['name']) < len(close_keys):
                        dict[topic['name'].upper()] = dict[close_keys]
                        del dict[close_keys]
                        close_keys = topic['name']
                else: close_keys = topic['name'].lower()
                if not close_keys in dict:
                    dict[close_keys] = (0,0)
                (a,b) = dict[close_keys]
                if topic['opinion'] == 'positive':
                    a += 1
                else: b += 1
                dict[close_keys] = (a,b)
    return dict

def pie_chart(df):
    raise NotImplementedError


def histogram_miss_tweet_number(df):
    raise NotImplementedError


def miss_pos_neg_data(df):
    raise NotImplementedError

print(misses_opinions())
