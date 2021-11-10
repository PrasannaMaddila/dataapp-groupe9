import argparse
from annotation_analysis import *

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]

dict_miss = misses_opinions()
keys = dict_miss.keys()


parser = argparse.ArgumentParser(
    description="Afficher les statistiques relatives à l'élection de la prochaine Miss France")
parser.add_argument("--histogram", action="store_true",
                    help="Display the histogram of all the competitors and their ratings in the Miss France competition")
parser.add_argument("--pie_chart_opinions", action="store_true",
                    help="Display the overall positivity of the competition")
parser.add_argument("Topic", type=str,
                    help="Display the information relative to a certain topic")
parser.add_argument("Individual_histogram", type="store_true")
parser.add_argument("Individual_pie_chart", type="store_true")

args = parser.parse_args()

print(keys)
if args.Topic == 'Miss France':
    print()
    if args.histogram:
        histogram(dict_miss)
    if args.pie_chart_opinions:
        pie_chart(corpus_dataframe)
elif args.Topic in keys:
    print("Choose the type of data you want")
    if args.Individual_histogram:
        individual_miss_graph_bar({args.Topic}, dict_miss)
    if args.Individual_pie_chart:
        individual_miss_graph_pie({args.Topic}, dict_miss)
