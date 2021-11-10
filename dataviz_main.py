from utils.annotation_analysis import  *

def main():
    dict_miss = misses_opinions()
    histogram(dict_miss)
    pie_chart(corpus_dataframe)

if __name__ == '__main__':
	main()
