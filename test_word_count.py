from word_count import remove_punct, num_word_count, sort_words

import pytest

def test_remove_punct():

    assert remove_punct(",") == ""
    assert remove_punct("-") == ""
    assert remove_punct(";") == ""

def test_num_word_count():

    assert num_word_count("A") == "a"
    assert num_word_count("S") == "s"

def test_sort_words():

    assert sort_words("alices") == 12
    assert sort_words("adventures") == 6
    
pytest.main(["-v", "--tb=line", "-rN", __file__])