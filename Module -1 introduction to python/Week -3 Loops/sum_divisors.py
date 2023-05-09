# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

def sum_divisors(number):
    # Initialize the appropriate variables
    divisor = 1
    total = 0

    # Avoid dividing by 0 and negative numbers
    # in the while loop by exiting the function
    # if "number" is less than one
    if number < 1:
        return 0

    # Complete the while loop
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        # Increment the correct variable
        divisor += 1

    # Return the correct variable
    return total


print(sum_divisors(0))  # Should print 0
print(sum_divisors(3))  # Should print 1
# 1
print(sum_divisors(36))  # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should print 1+2+3+6+17+34+51
# 114
