def get_remainder(x, y):

    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder


print(get_remainder(10, 3))
