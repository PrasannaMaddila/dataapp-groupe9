import matplotlib.pyplot as plt

def words_graph(dict):
    words = []
    for item in dict.items():
        words.append((item[1],item[0]))
    words.sort()
    words.reverse()
    if len(words) > 40:
        words = words[:40]

    # Now to plot the graph
    labels = [item[1] for item in words]
    heights = [item[0] for item in words]

    plt.bar(labels, heights)
    plt.title("Words frequencies")
    # plt.xticks(rotation=45, ha="right")
    plt.show()

def test():
    words_graph({"hello": 3, "yes": 2})

test()