import argparse
from annotation_analysis import *

dict_miss = misses_opinions()
keys = dict_miss.keys()

parser = argparse.ArgumentParser(
    description="Afficher les statistiques relatives à l'élection de la prochaine Miss France")

parser.add_argument("-H", "--histogram", action="store_true",
                    help="Display the histogram of all the competitors and their ratings in the Miss France competition")
parser.add_argument("-P", "--pie_chart_opinions", action="store_true",
                    help="Display the overall positivity of the competition")
parser.add_argument("-T", "--Topic", type=str,
                    help="Display the information relative to a certain topic")
parser.add_argument("-I", "--Individual_histogram", action='count', default=0)
parser.add_argument("-Ip", "--Individual_pie_chart", action='count', default=0)

args = parser.parse_args()
if args.Topic == 'Miss France':
    print("Information relative to the Miss France competion")
    if args.histogram:
        histogram(dict_miss)
    elif args.pie_chart_opinions:
        pie_chart(corpus_dataframe)
elif args.Topic in keys:
    print("Choose the type of data you want for a Miss")
    if args.Individual_histogram == 1:
        individual_miss_graph_bar(args.Topic, dict_miss)
    if args.Individual_pie_chart == 1:
        individual_miss_graph_pie(args.Topic, dict_miss)
