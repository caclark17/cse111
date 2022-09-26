"""
File: test_names.py
Author: Adam Ulrich
purpose: test names functions

Write test_make_full_name so that it tests make_full_name with various names, including long names, short names, and hyphenated names. Fix the mistake in the make_full_name function.
 * I assert that looking at the function, long and short names, hyphenated names will not currently make a difference. If the implementation changes in the future, then it is possible.
 * I assert that the function handles empty strings poorly.

Write test_extract_family_name so that it tests extract_family_name with various names, including long names, short names, and hyphenated names.
Write test_extract_given_name so that it tests extract_given_name with various names, including long names, short names, and hyphenated names. Fix the mistake in the extract_given_name function.
"""
from address import extract_city, extract_state, extract_zipcode

from names import make_full_name, \
    extract_family_name, extract_given_name

import pytest

def test_make_full_name():
    """
    Write assert statements inside this function to test the value returned from the make_full_name function. 
    If you are not sure what the make_full_name function does or how to test it, 
    read the documentation string that is at the top of the make_full_name function in the names.py file.
    """
    assert make_full_name("Joseph", "Smith") == "Smith; Joseph"
    assert make_full_name("","Ulrich-Ruiz") == "Ulrich-Ruiz; "
    assert make_full_name("Abetonga","Bonteman") == "Bonteman; Abetonga"
    assert make_full_name("Edisson","Ruiz") == "Ruiz; Edisson"
    assert make_full_name("Richard", "Van Leuwen") == "Van Leuwen; Richard"
  
def test_extract_family_name ():
    """
    Write assert statements inside this function to test the value returned from the extract_family_name function.
    """
    assert extract_family_name("Young-Smith; Brigham") == "Young-Smith"
    assert extract_family_name(make_full_name("Joseph", "Smith")) == "Smith"
    assert extract_family_name(make_full_name("Edisson", "Ruiz")) == "Ruiz"
    assert extract_family_name("; ") == ""
    assert extract_family_name("Johnson; ") == "Johnson"
    assert extract_family_name("; Beyonce") == ""
    assert extract_family_name("Bonteman; Moanarita") == "Bonteman"

    
def test_extract_given_name():

    """
    Write assert statements inside this function to test the value returned from the extract_given_name function.
    """

    assert extract_given_name(make_full_name("Leandro", "Ruiz")) == "Leandro"
    assert extract_given_name("Young-Smith; Brigham") == "Brigham"
    assert extract_given_name(make_full_name("Joseph", "Smith")) == "Joseph"
    assert extract_given_name(make_full_name("Edisson", "Ruiz")) == "Edisson"


def test_extract_state():
    
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("60 NW Temple St, Salt Lake City, UT 84150") == "UT"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"


def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("60 NW Temple St, Salt Lake City, UT 84150") == "84150"
    assert extract_zipcode("11821 SE 282nd St, Auburn, WA 98092-0001") == "98092-0001"

def test_extract_city():

    assert extract_city("11821 SE 282nd St, Auburn, WA 98092") == "Auburn"
    assert extract_city(" 60 NW Temple St, Salt Lake City, UT 84150") == "Salt Lake City" 
  
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])