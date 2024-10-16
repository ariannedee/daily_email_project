from helpers import c_to_f, f_to_c


def test_c_to_f():
    assert c_to_f(0) == 32
    assert round(c_to_f(36.5)) == 98


def test_f_to_c():
    assert f_to_c(32) == 0
    assert round(f_to_c(98), 2) == 36.67
