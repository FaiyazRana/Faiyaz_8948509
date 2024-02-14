import functions

def test_reversed_str():
    assert functions.reverse_string("HELLO") == "OLLH"


def test_factorial():
    assert functions.factorial(4) == 24