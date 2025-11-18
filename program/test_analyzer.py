import pytest

from analyzer import count_words, count_chars, find_most_common_word

def test_count_words():
    assert count_words("this is a test") == 4
    assert count_words("count words function") == 3
    assert count_words("") == 0
    assert count_words("       ") == 0

def test_count_chars():
    assert count_chars("testing, testing") == 16
    assert count_chars("count chars function") == 20
    assert count_chars("") == 0
    assert count_chars("     ") == 5

def test_find_most_common_word():
    assert find_most_common_word("this is a test for a function") == "a"
    assert find_most_common_word("to be or not to be") == "to"