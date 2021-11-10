import matplotlib.pyplot as plt
import pandas as pd
from difflib import *
from pytest import *
import json
from corpus_statistics import nb_negative_opinions, nb_positive_opinions
import numpy as np


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
                    dict[close_keys] = (0, 0)
                (a, b) = dict[close_keys]
                if topic["opinion"] == "positive":
                    a += 1
                else:
                    b += 1
                dict[close_keys] = (a, b)
    return dict


def pie_chart(df=corpus_dataframe):
    pos = nb_positive_opinions(df)
    neg = nb_negative_opinions(df)
    labels = 'Positive opinion proportion', 'Negative opinion proportion'
    sizes = [pos, neg]
    explode = (0.1, 0)
    colors = ['g', 'r']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels,
            autopct='%1.1f%%', colors=colors, shadow=True, startangle=90, wedgeprops={'linewidth': 5})
    ax1.axis('equal')
    plt.show()


# pie_chart()


def histogram(df=corpus_dataframe):

    test = {'Ms Jean-Marie Lafayette': (99, 3), 'Mr Jean Luc Mélenchon': (
        50, 50), 'Ghandi the Wise': (98, 2)}
    pos, neg = [], []
    label = []
    n = len(test)
    ind = np.arange(n)
    width = 0.5
    for key in test.keys():
        pos.append(test[key][0])
        neg.append(test[key][1])
        label.append(key)
    p1 = plt.bar(ind, neg, width, color='r')
    p2 = plt.bar(ind, pos, width, color='g')
    plt.ylabel('Opinions')
    plt.title('Opinions on Miss France')
    plt.xticks(ind, label)
    plt.legend((p1[0], p2[0]), ['Negative', 'Positive'])
    plt.show()


histogram()


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
