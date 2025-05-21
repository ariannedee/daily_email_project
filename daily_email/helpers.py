def c_to_f(temp):
    return round((temp * 9 / 5) + 32)


def test_c_to_f():
    assert c_to_f(0) == 32
    assert c_to_f(36.5) == 97
