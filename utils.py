# This file currently contains the read_and_load function


def read_and_load_annotation(filename="143048389142134785.ann"):
    # Reading the contents of the file
    with open(filename) as f:
        lines = f.readlines()
        # topic_dict_template = {"name": , "opinion": }
        parsed_dict = {"topic": [], "positive_keywords": [], "negative_keywords": []}
        word_list = {}
        # Processing the Title lines
        for line in lines:
            if line[0] == "T":
                if "Topic" in line:
                    word_list[line[0:2]] = {"word": line.split()[-1], "type": "topic"}
                elif "positive" in line.lower():
                    word_list[line[0:2]] = {
                        "word": line.split()[-1],
                        "type": "positive",
                    }
                elif "negat" in line.lower():
                    word_list[line[0:2]] = {
                        "word": line.split()[-1],
                        "type": "negative",
                    }
        # print(word_list)
        # processing the Relation lines
        key_word = ""
        for line in lines:
            if line[0] != "R":
                continue
            words = line.split()
            if "positive" in words[1].lower():
                print("+ve\n")
                # Processing each word in the line, T3, T4 etc.
                for word in words[2:]:
                    key_word = word.partition(":")[2]
                    if "topic" in word_list[key_word]["type"]:
                        parsed_dict["topic"].append(
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
            else:
                # Negative word insert.
                for word in words[2:]:
                    key_word = word.partition(":")[2]
                    ## ADD: case for Negates: combine the words
                    ##      case for isNegative: just add
                    # Not working now!!!!

                    if word_list[key_word]["type"] == "topic":
                        parsed_dict["topic"].append(
                            {
                                "name": word_list[key_word]["word"],
                                "opinion": "negative",
                            }
                        )
                    else:
                        parsed_dict[word_list[key_word]["type"] + "_keywords"].append(
                            word_list[key_word]["word"]
                        )
                    # end of if-insert-negative
                # end of for

            # Checking to see what we've got
        print(parsed_dict)

        # Reading for topic

    return parsed_dict
    raise NotImplementedError


# Test for read_and_load():
# from datavisualization.corpusutils import read_and_load_annotation
from pytest import *

"""
if "Topic" in line:
                print("found topic")
                parsed_dict["topic"].append({"name": line.split()[-1], "opinion": ""})
            elif "Subjectiveme_positive" in line:
                print("Found +ve word.")
                parsed_dict["positive_keywords"].append(line.split()[-1])
            elif "Negator" in line:
                print("Found -ve word.")
                parsed_dict["negative_keywords"].append(line.split()[-1]) """


def test_read_and_load_annotation():
    # Given
    filename = "143048389142134785.ann"
    # When
    annotations = read_and_load_annotation(filename)
    # Then
    assert annotations == {
        "topics": [{"name": "élection de #missfrance", "opinion": "negative"}],
        "negative_keywords": ["pas plaisir"],
        "positive_keywords": ["plaisir"],
    }
    # Given
    filename1 = "143059118180139008.ann"
    # When
    annotations1 = read_and_load_annotation(filename1)
    # Then
    assert annotations1 == {
        "topics": [
            {"name": "Languedoc", "opinion": "positive"},
            {"name": "Nord-Pas-De-Calais", "opinicon": "negative"},
        ],
        "negative_keywords": ["pas aime"],
        "positive_keywords": ["jolie", "aime"],
    }


read_and_load_annotation()
# test_read_and_load_annotation()
