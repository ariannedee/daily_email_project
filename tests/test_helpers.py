try:
    from helpers import c_to_f
except ImportError:
    from daily_email.helpers import c_to_f


def test_c_to_f_at_0():
    assert c_to_f(0) == 32

def test_c_to_f_at_body_temp():
    assert round(c_to_f(36.5)) == 98
