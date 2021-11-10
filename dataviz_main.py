from utils import annotations_analysis

def main():
	dict_miss = misses_opinions()
    dict_miss.pop("miss")
    histogram(dict_miss)
    pie_chart(corpus_dataframe)

if __name__ == '__main__':
	main()
