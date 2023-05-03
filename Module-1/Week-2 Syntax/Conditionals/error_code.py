def translate_error_code(error_code):

    # The if-elif-else block assesses the value of the variable
    # passed to the function as a parameter. The if statement uses
    # the equality operator == to test the value of the variable.
    # This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
        # If the comparison above returns True, then the indented
        # line(s) inside the if-statement will run. In this case, the
        # action is to assign a string to the translation variable.
        # The remainder of the if-elif-else block will not run.
        # The Python interpreter will skip to the next line outside of
        # the if-elif-else block. In this case, the next line is the
        # return value statement.
        translation = "Server received an unauthenticated request"

# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
        # If the first elif-statement returns a True result, then the
        # indented line(s) inside the first elif-statement will run.
        # After this line, the remainder of the if-elif-else block will
        # not run. The Python interpreter will skip to the next line
        # outside of the if-elif-else block.
        translation = "Requested web page not found on server"

# If both the initial if-statement and the first elif-statement
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
        # If the second elif-statement returns a True result, then the
        # indented line(s) inside the second elif-statement will run.
        # After this line, the remainder of the if-elif-else block will
        # not run. The Python interpreter will skip to the next line
        # outside of the if-elif-else block.
        translation = "Server request to close unused connection"

# If the conditional tests above do not produce a True result
# then the else-statement will run.
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation


print(translate_error_code("404 Not Found"))
