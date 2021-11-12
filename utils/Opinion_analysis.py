from pandas.core.frame import DataFrame
from textblob import TextBlob
import pandas as pd
from difflib import *
import json

corpus_dataframe = pd.read_csv("./utils/corpus_dataframe.csv", header=0)


def opinion_of_event(df=corpus_dataframe):
    pos, neu, neg = 0, 0, 0
    for tweet in df['text']:
        opinion = TextBlob(tweet).sentiment.polarity
        if opinion > (1/3):
            pos += 1
        if opinion < -(1/3):
            neg += 1
        else:
            neu += 1
    nbr_tweets = pos + neu + neg
    print("Percentage of positive tweets: {}%".format(pos*100/nbr_tweets))
    print("Percentage of neutral tweets: {}%".format(neu*100/nbr_tweets))
    print("Percentage of negative tweets: {}%".format(neg*100/nbr_tweets))


def misses_tweets(df=corpus_dataframe):
    dict = {}
    for i in range(len(df["annotations"])):
        ann = df["annotations"][i]
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
            if len(words) < 2:
                continue
            if words[0] == "miss":
                close_keys = get_close_matches(
                    topic["name"].lower()[5:], [k[5:]
                                                for k in dict.keys()], 1, 0.6
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
                    dict[close_keys] = []
                dict[close_keys] = dict[close_keys] + [i]

    return dict


print(misses_tweets())


def opinion_on_miss(miss, df=corpus_dataframe):
    dict_tweets = misses_tweets(df)
    tweets = dict_tweets[miss]
    pos, neu, neg = 0, 0, 0
    for line_nb in tweets:
        tweet = df['text'][line_nb]
        opinion = TextBlob(tweet).sentiment.polarity
        if opinion > (1/3):
            pos += 1
        if opinion < -(1/3):
            neg += 1
        else:
            neu += 1
    nbr_tweets = pos + neu + neg
    print("Percentage of positive tweets: {}%".format(pos*100/nbr_tweets))
    print("Percentage of neutral tweets: {}%".format(neu*100/nbr_tweets))
    print("Percentage of negative tweets: {}%".format(neg*100/nbr_tweets))


opinion_on_miss('miss tahiti')
