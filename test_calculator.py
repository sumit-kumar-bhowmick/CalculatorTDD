from calculator import add


def test_add_empty_string():
    # test for empty string as the input
    assert add("") == 0


def test_add_single_number():
    # test for single number as input
    assert add("1") == 1
    assert add("12") == 12
    assert add("123") == 123
