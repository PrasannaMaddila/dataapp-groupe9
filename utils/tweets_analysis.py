import matplotlib.pyplot as plt

def words_graph(dict):
    words = []
    for item in dict.items():
        words.append((item[1],item[0]))
    words.sort()
    words.reverse()
    if len(words) > 40:
        words = words[:40]
    print(words)

    # Now to plot the graph

    colors = ["cyan", "red"]

    # plt.bar(labels, heights, color=colors)
    # plt.title("Words frequencies" , words, frequencies))
    # plt.xticks(rotation=45, ha="right")
    # plt.show()

def test():
    words_graph({"hello": 3, "yes": 2})

test()