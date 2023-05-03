"""
name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky numer is " + str(number))

name = "Borja"
number = len(name) * 9

print("Hello " + name + ". Your lucky numer is " + str(number))
"""


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky numer is " + str(number))


lucky_number("Kay")
lucky_number("Borja")
