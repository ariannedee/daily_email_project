def c_to_f(temp_c, decimals=1):
    temp_f = (temp_c * 9 / 5) + 32
    return round(temp_f, decimals)


def f_to_c(temp_f, decimals=1):
    temp_c = (temp_f - 32) * 5 / 9
    return round(temp_c, decimals)
