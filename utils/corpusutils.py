from _pytest.mark import KeywordMatcher
import numpy as np
import pandas as pd
from pytest import *


datadir = "../Data/"
annodir = datadir + "tweets-annotations/part-0/"
tweetdir = datadir + "tweets/"


def read_and_load_ann_annotation(filename="143059118180139008.ann"):
    # Reading the contents of the file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # This is the structure that we need, so
        # we create an empty version.
        parsed_dict = {
            "topics": [],
            "negative_keywords": [],
            "positive_keywords": [],
        }
        # Processing the Title lines
        # and creating a list of the words that
        # we will use later.
        word_list = {}
        for line in lines:
            if line[0] == "T":
                if "Topic" in line:
                    word_list[line[0:2]] = {
                        "word": " ".join(line.split()[4:]),
                        "type": "topics",
                    }
                elif "positive" in line.lower():
                    word_list[line[0:2]] = {
                        "word": line.split()[-1].lower(),
                        "type": "positive",
                    }
                elif "negat" in line.lower():
                    word_list[line[0:2]] = {
                        "word": line.split()[-1].lower(),
                        "type": "negative",
                    }
        # print(word_list)

        # processing the Relation lines :
        # Here, we create the actual list of parsed words,
        # depending on if they're +ve, -ve etc.
        key_word = ""
        for line in lines:
            # Ignore any Title lines - we've
            # already gone through them
            if line[0] != "R":
                continue

            # Getting each word.
            words = line.split()

            # Now, if its a positive Relation, use this section:
            if "positive" in words[1].lower():
                for word in words[2:]:
                    key_word = word.partition(":")[2]
                    if "topic" in word_list[key_word]["type"]:
                        parsed_dict["topics"].append(
                            {
                                "name": word_list[key_word]["word"],
                                "opinion": "positive",
                            }
                        )
                    else:
                        parsed_dict["positive_keywords"].append(
                            word_list[key_word]["word"]
                        )
                    # end of if-insert-positive
                # end of for
            elif "Negates" in words[1]:
                # Negative word insert for keyword "Negates".
                # If the word is "Negates", concatenate all neg.words
                # into one entry, and don't check for word type.
                key_word = [word.partition(":")[2] for word in words[2:]]
                negative_entries = []
                for key in key_word:
                    negative_entries.append(word_list[key]["word"])

                parsed_dict["negative_keywords"].append(
                    " ".join(negative_entries))
            elif "Negative" in words[1]:
                # Here, we check the case of the word.
                # If word is TOPIC: insert into negative anyway.
                # Else: insert into "word_type"_keywords i.e. insert into
                # the type of the word
                words = line.split()
                for word in words[2:]:
                    key_word = word.partition(":")[2]
                    if "topics" in word_list[key_word]["type"]:
                        parsed_dict["topics"].append(
                            {
                                "name": word_list[key_word]["word"],
                                "opinion": "negative",
                            }
                        )
                    else:
                        # It is not a topic, and we need to check its type
                        parsed_dict[word_list[key_word]["type"] + "_keywords"].append(
                            word_list[key_word]["word"]
                        )
                    # end of if-insert-negative
                # end of for """

            # Checking to see what we've got
        """ print("The Parsed Dictionary is: \n")
        print(parsed_dict)
        print("\n") """
        # Reading for topic

    return parsed_dict


# Test for read_and_load():
# from datavisualization.corpusutils import read_and_load_annotation

# This is the test for our function above.


def test_read_and_load_annotation():
    # Given
    filename = "143048389142134785.ann"
    # When
    annotations = read_and_load_ann_annotation(filename)
    # Then
    assert annotations == {
        "topics": [{"name": "élection de #missfrance", "opinion": "negative"}],
        "negative_keywords": ["pas plaisir"],
        "positive_keywords": ["plaisir"],
    }
    # Given
    filename1 = "143059118180139008.ann"  # "143048389142134785.ann"  #
    # When
    annotations1 = read_and_load_ann_annotation(filename1)
    # Then
    assert annotations1 == {
        "topics": [
            {"name": "Languedoc", "opinion": "positive"},
            {"name": "Nord-Pas-De-Calais", "opinion": "negative"},
        ],
        "negative_keywords": ["pas aime"],
        "positive_keywords": ["jolie", "aime"],
    }


def load_tweet_with_annotation(id):
    S = read_and_load_ann_annotation(annodir + id + ".ann")
    if S == {}:
        return "No annotations"
    else:
        res = {}
        res["id"] = id
        res["text"] = open(tweetdir + id + ".txt", "r",
                           encoding="utf-8").read()
        res["annotations"] = S
        return res


def test_load_tweet_with_annotation():
    id = "143048389142134785"
    dict = load_tweet_with_annotation(id)
    assert dict == {
        "id": "143048389142134785",
        "text": "Ce soir c'est l'élection de #missfrance et je vais me faire un plaisir de NE PAS regarder.",
        "annotation": {
            "topics": [
                {"name": "Languedoc", "opinion": "positive"},
                {"name": "Nord-Pas-De-Calais", "opinicon": "negative"},
            ],
            "negative_keywords": ["pas aime"],
            "positive_keywords": ["jolie", "aime"],
        },
    }
    id = "143049242305495040"
    dict = load_tweet_with_annotation(id)
    assert dict == "No annotations"


def load_corpus_in_dataframe():
    ids = open(datadir + "tweets-ids").readlines()
    dict = {}
    dict["id"] = []
    dict["text"] = []
    dict["annotations"] = []
    for id in ids:
        try:
            temp = load_tweet_with_annotation(id[:-1])
            if temp != "No annotations":
                dict["id"].append(temp["id"])
                dict["text"].append(temp["text"])
                dict["annotations"].append(temp["annotations"])
        except:
            continue

    return pd.DataFrame.from_dict(dict)


corpus_dataframe = load_corpus_in_dataframe()
corpus_dataframe.to_csv("./corpus_dataframe.csv")  # For repeated use later
# print(corpus_dataframe)
