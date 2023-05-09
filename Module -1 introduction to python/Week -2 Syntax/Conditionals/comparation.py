# Sets value of the "number" variable
number = 25

# The "number" variable will first be compared to 5. Since it is
# False that "number" is not less than or equal to 5, the expression indented
# under this line will be ignored.
if number <= 5:
    print("The number is 5 or smaller.")

# Next, the "number" variable will be compared to 33. Since it is
# False that "number" is equal to 33, the expression indented under
# this line will be ignored.
elif number == 33:
    print("The number is 33.")

# Then, the "number" variable will be compared to 32 and 6. Since it
# is True that 25 is less than 32 and greater than 6, the Python
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")

else:
    print("The number is " + str(number))

# Expected output is:
# The number is less than 32 and greater than 6.
