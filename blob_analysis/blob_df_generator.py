from textblob import TextBlob
import pandas as pd

import nltk.data

# chargement du tokenizer
try:
    tokenizer = nltk.data.load("tokenizers/punkt/french.pickle")
    print("French worked")
except:
    print("French didn't work")

word = TextBlob("Hello World!")
print(word.sentiment)

df_path = "./corpus_dataframe.csv"
corpus_dataframe = pd.read_csv("./utils/corpus_dataframe.csv", header=0)


def create_sentiment_df(df):
    blob_dataframe = pd.DataFrame()
    id, temp = 0, []
    for index, row in df.iterrows():  # id, tweet in df["id"], df["text"]:
        id = row["id"]
        temp = TextBlob(row["text"])
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
