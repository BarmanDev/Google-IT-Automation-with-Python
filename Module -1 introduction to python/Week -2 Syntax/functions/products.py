
# Example 1
# Evaluate the output of this print statement

def product(a, b):
    return (a*b)


print(product(product(2, 4), product(3, 5)))

#################################

# Example 2
# Evaluate the output of this print statement


def difference(a, b):
    return (a-b)


def sum(a, b):
    return (a+b)


print(difference(sum(2, 2), sum(3, 3)))


#################################


# Example 3
# Evaluate the Boolean output of this comparison


# Example 3
# Evaluate the Boolean output of this comparison


print((5 >= 2*4) and (5 <= 4*3))


#################################


# Example 4
# Evaluate the value of the comparison in the if statement


x = 3
if x+5 > x**2 or x % 4 != 0:
    print("This comparison is True")


#################################


# Example 5
# Evaluate the output of this if-elif-else statement


number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)


# Click Run to check your answers. If you are having trouble
# calculating the correct answers manually, please review the
# Practice Quiz Study Guides, videos, and readings in this Module.
