def c_to_f(temp_c: float) -> float:
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Expected 32 but got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Expected 98 but got {round(c_to_f(36.5))}"
