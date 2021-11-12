from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import pandas as pd
from ast import literal_eval
from pytest import *
import json

blob_dataframe = pd.read_csv("./blob_dataframe.csv", header=0, encoding="utf-8")
# blob_dataframe = blob_dataframe.iloc[:, 1:]


def nb_tweets():
    return len(open("./Data/tweets-ids").readlines())


def nb_sentiment(df=blob_dataframe):
    return len(df["sentiment"])


""" def nb_subjects(df=blob_dataframe):
    # return [ann_dict["topics"] for ann_dict in len(blob_dataframe["sentiment"])
    return len(subjects(df)) """


""" def subjects(df=blob_dataframe):
    subs = []
    for ann in df["sentiment"]:
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
 """


def nb_opinions(df=blob_dataframe):
    pos, neg, neu = 0, 0, 0
    temp_tup = []
    for senti_tup in df["sentiment"]:
        temp_tup = literal_eval(senti_tup)
        if temp_tup[0] <= -1 / 3:
            neg += 1
        elif temp_tup[0] <= 1 / 3:
            neu += 1
        else:
            pos += 1
    return (pos, neu, neg)


if __name__ == "__main__":
    tup = nb_opinions(blob_dataframe)
    num_tweets_blob = nb_sentiment()
    print("Percentage of positive tweets: {}%".format(tup[0] * 100 / num_tweets_blob))
    print("Percentage of neutral tweets: {}%".format(tup[1] * 100 / num_tweets_blob))
    print("Percentage of negative tweets: {}%".format(tup[2] * 100 / num_tweets_blob))
    print("Sum of all percentages = {}%".format(sum(tup) * 100 / num_tweets_blob))
