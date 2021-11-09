import matplotlib.pyplot as plt
import pandas as pd
from corpus_statistics import nb_negative_opinions, nb_positive_opinions
import numpy as np

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]


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
    fig = plt.figure()
    ax = fig.add_axes()
    p1 = plt.bar(ind, neg, width, color='r')
    p2 = plt.bar(ind, pos, width, color='g')
    plt.ylabel('Opinions')
    plt.title('Opinions on Miss France')
    plt.xticks(ind, label)
    plt.legend((p1[0], p2[0]), ['Negative', 'Positive'])
    plt.show()


histogram()
