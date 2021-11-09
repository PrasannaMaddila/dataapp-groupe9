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
    for ann in df["annotations"]:
        ann = json.loads(ann.replace("'", '"'))
        for topic in ann["topics"]:
            if (
                topic == []
                or "france" in topic["name"].lower()
                or "miss" not in topic["name"].lower()
            ):
                continue
            words = topic["name"].lower().split()
            topic["name"] = topic["name"].replace("-", " ")
            if words[0] == "miss":
                close_keys = get_close_matches(
                    topic["name"].lower()[5:], [k[5:] for k in dict.keys()], 1, 0.6
                )
                if close_keys:
                    close_keys = "miss " + close_keys[0]
                    # min_len = min(len(close_keys), len(topic['name']))
                    if len(topic["name"]) < len(close_keys):
                        dict[topic["name"].lower()] = dict[close_keys]
                        del dict[close_keys]
                        close_keys = topic["name"].lower()
                else:
                    close_keys = topic["name"].lower()
                if not close_keys in dict:
                    dict[close_keys] = (0, 0)
                (a, b) = dict[close_keys]
                if topic["opinion"] == "positive":
                    a += 1
                else:
                    b += 1
                dict[close_keys] = (a, b)
    return dict


def pie_chart(df):
    raise NotImplementedError


def histogram_miss_tweet_number(dict_miss):
    for key in dict_miss.keys():
        pos_data = dict_miss[key][0]
        neg_data = dict_miss[key][1]

    print(pos_data)
    print("\n")
    print(neg_data)


def miss_pos_neg_data(df):
    raise NotImplementedError


dict_miss = misses_opinions()
print(dict_miss)
histogram_miss_tweet_number(dict_miss)
