from calculator import add


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


