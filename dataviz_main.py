from utils.annotation_analysis import  *
from utils.corpus_statistics import *
from utils.tweets_analysis import *

def main():
    dict_miss = misses_opinions()
    histogram(dict_miss)
    pie_chart(corpus_dataframe)
    words_graph(corpus_frequent_words())

if __name__ == '__main__':
	main()
