# This file currently contains the read_and_load function


def read_and_load_annotation():
    raise NotImplementedError


# Test for read_and_load():
# from datavisualization.corpusutils import read_and_load_annotation
from pytest import *


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


test_read_and_load_annotation()
