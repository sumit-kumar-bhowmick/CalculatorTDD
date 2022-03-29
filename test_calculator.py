from calculator import add
import pytest


def test_add_empty_string():
    # test for empty string as the input
    assert add("") == 0


def test_add_single_number():
    # test for single number as input
    assert add("1") == 1
    assert add("12") == 12
    assert add("123") == 123


def test_add_two_input_string():
    # test for two number separated by ,
    assert add("1,2") == 3
    # test for two number separated by \n
    assert add("1\n2\n") == 3


def test_add_multiple_numbers_input():
    # test for multiple numbers as input.(i.e >2 numbers).
    assert add("1,2,3,4") == 10
    assert add("1\n2\n3\n4") == 10


def test_add_with_deliminator():
    # test with deliminator
    assert add(";\n1\n2\n3") == 6
    assert add(';\n2;12;5') == 19


def test_add_not_allowed_separator():
    # test for not allowing , and \n together as separator
    assert add(
        "1,\n") == f'''wrong input,the input contain "\\n," or ",\\n".provide any one of them as separator.ie , or \\n'''
    assert add(
        "1,\n2,\n3") == f'''wrong input,the input contain "\\n," or ",\\n".provide any one of them as separator.ie , or \\n'''
    assert add(
        "1\n,2,\n3") == f'''wrong input,the input contain "\\n," or ",\\n".provide any one of them as separator.ie , or \\n'''


def test_add_negative_input():
    # test for negative numbers as input
    with pytest.raises(ValueError):
        add("-1,2,3")

    with pytest.raises(ValueError):
        add("-1,-2,3")

    with pytest.raises(ValueError):
        add("-1\n-2\n3")

    with pytest.raises(ValueError):
        add(";\n-1;-2;3")


def test_add_none_input():

    add(None) == -1


