from .weather import c_to_f


def test_0():
    assert c_to_f(0) == 32


def test_body_temp():
    assert round(c_to_f(36.5)) == 98
