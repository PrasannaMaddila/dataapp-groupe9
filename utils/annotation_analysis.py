import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
#from utils.corpus_statistics import nb_negative_opinions, nb_positive_opinions
import numpy as np
from difflib import *
from pytest import *
import json
import seaborn as sns


corpus_dataframe = pd.read_csv("./utils/corpus_dataframe.csv")
corpus_miss_opinions = pd.read_csv("corpus miss opinions.csv")
# corpus_dataframe = corpus_dataframe.iloc[:, 1:]

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
                    dict[close_keys] = (0, 0)
                (a, b) = dict[close_keys]
                if topic["opinion"] == "positive":
                    a += 1
                else:
                    b += 1
                dict[close_keys] = (a, b)
    return dict


''' def pie_chart(df=corpus_dataframe):
    pos = nb_positive_opinions(df)
    neg = nb_negative_opinions(df)
    labels = "Positive opinion proportion", "Negative opinion proportion"
    sizes = [pos, neg]
    explode = (0.1, 0)
    colors = ["g", "r"]

    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors,
        shadow=True,
        startangle=90,
        wedgeprops={"linewidth": 5},
    )
    ax1.axis("equal")
    plt.show()
 '''


def histogram(df=corpus_dataframe):
    """test = {
        "Ms Jean-Marie Lafayette": (99, 3),
        "Mr Jean Luc Mélenchon": (50, 50),
        "Ghandi the Wise": (98, 2),
    }"""
    pos, neg = [], []
    label = []
    n = len(df)
    ind = np.arange(n)
    width = 0.8  # Changed from 0.5
    for key in df.keys():
        pos.append(df[key][0])
        neg.append(df[key][1])
        label.append(key)
    fig = plt.figure()
    ax = fig.add_axes()
    p1 = plt.bar(
        ind, [neg[index] + pos[index] for index in range(len(neg))], width, color="r"
    )
    p2 = plt.bar(ind, pos, width, color="g")
    plt.ylabel("Opinions")
    plt.title("Opinions on Miss France")
    plt.xticks(ind, [string.title() for string in label])
    plt.legend((p1[0], p2[0]), ["Negative", "Positive"])
    plt.xticks(rotation=45, ha="right")
    plt.show()


def individual_miss_graph_pie(miss_name, dict):
    key = get_close_matches(miss_name.lower(), dict.keys(), 1, 0.6)[0]
    # Now that we have the key, we can plot her data.
    labels = ["Positive", "Negative"]
    print(key)

    # Now to plot the graph
    pos = dict[key][0]
    neg = dict[key][1]
    labels = ["Positive", "Negative"]
    sizes = [pos, neg]
    explode = (0.1, 0)
    colors = ["g", "r"]

    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors,
        shadow=True,
        startangle=90,
        wedgeprops={"linewidth": 5},
    )
    ax1.axis("equal")
    plt.title("Opinions on {0}: +{1}, -{2}".format(key.title(), pos, neg))
    plt.show()


def individual_miss_graph_bar(miss_name, dict):
    key = get_close_matches(miss_name.lower(), dict.keys(), 1, 0.6)[0]
    # Now that we have the key, we can plot her data.
    labels = ["Positive", "Negative"]
    print(key)

    # Now to plot the graph
    pos = dict[key][0]
    neg = dict[key][1]
    labels = ["Positive", "Negative"]
    heights = [pos, neg]
    colors = ["green", "red"]

    plt.bar(labels, heights, color=colors)
    plt.title("Opinions on {0}: +{1}, -{2}".format(key.title(), pos, neg))
    plt.xticks(rotation=45, ha="right")
    plt.show()


""" def miss_pos_neg_data(df):
    raise NotImplementedError
 """

if __name__ == "__main__":
    # Main execution loop: driver code
    dict_miss = misses_opinions()
    """ histogram(dict_miss)
    pie_chart(corpus_dataframe)
    individual_miss_graph_pie("reunion", dict_miss)
    """
    individual_miss_graph_bar("reunion", dict_miss)


def seaborn_histogramm(df=corpus_miss_opinions):
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(6, 15))

    sns.set_color_codes("muted")
    sns.barplot(x="2", y="0", data=df,
                label="Neutral", color="orange")

    sns.set_color_codes("pastel")
    sns.barplot(x="1", y="0", data=df,
                label="Positive", color="g", alpha=0.5)

    sns.set_color_codes("muted")
    sns.barplot(x="3", y="0", data=df,
                label="Negative", color="r", alpha=0.5)

    ax.legend(ncol=3, loc="lower right", frameon=True)
    ax.set(xlim=(0, 24), ylabel="",
           xlabel="Number of opinions")
    sns.despine(left=True, bottom=True)
    plt.show()


seaborn_histogramm()
