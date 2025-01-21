def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


if __name__ == '__main__':
    assert c_to_f(0) == 32, f'Expected 32 but got {c_to_f(0)}'
    assert round(c_to_f(36.7)) == 98, f'Expected 98 but got {round(c_to_f(36.7))}'
    print('All tests passed')
