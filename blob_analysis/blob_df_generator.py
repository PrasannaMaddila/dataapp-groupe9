from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import pandas as pd

## This file generates the analysis of the tweets in the
## corpus using the pre-existing dataframe, and runs
## it through textblob-fr.

## NOTE: Run this program in the root git folder to
## regenerate blob_dataframe in the correct location.

df_path = "./corpus_dataframe.csv"
corpus_dataframe = pd.read_csv("./utils/corpus_dataframe.csv", header=0)


def create_sentiment_df(df):
    blob_dataframe = pd.DataFrame()
    id, temp = 0, []
    for index, row in df.iterrows():  # id, tweet in df["id"], df["text"]:
        id = row["id"]
        temp = TextBlob(
            row["text"], pos_tagger=PatternTagger(), analyzer=PatternAnalyzer()
        )
        blob_dataframe = blob_dataframe.append(
            {
                "id": str(id),
                "text": temp,
                "sentiment": temp.sentiment,
                "nouns": temp.noun_phrases,
            },
            ignore_index=True,
        )
    return blob_dataframe


create_sentiment_df(corpus_dataframe).to_csv("./blob_dataframe.csv")
