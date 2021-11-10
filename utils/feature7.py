import argparse
from annotation_analysis import *

dict_miss = misses_opinions()


parser = argparse.ArgumentParser(
    description="Afficher les statistiques relatives à l'élection de la prochaine Miss France")
parser.add_argument("--histogram", action="store_true")
args = parser.parse_args()

if args.histogram:
    histogram(dict_miss)
