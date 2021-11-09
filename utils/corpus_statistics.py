# import numpy as np
import pandas as pd
from pytest import *

corpus_dataframe = pd.read_csv("./corpus_dataframe.csv")
corpus_dataframe = corpus_dataframe.iloc[:, 1:]
print(corpus_dataframe)
