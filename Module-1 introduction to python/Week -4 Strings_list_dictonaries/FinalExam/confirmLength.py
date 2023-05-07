"""
Fill in the blanks to complete the “confirm_length” function. 
This function should return how many characters a string contains as long as it has one
or more characters, otherwise it will return 0. Complete the string operations needed in this function
so that input like "Monday" will produce the output "6".
"""


def confirm_length(word):

    # Complete the condition statement using a string operation.
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a"))  # Should print 1
print(confirm_length("This is a long string"))  # Should print 21
print(confirm_length("Monday"))  # Should print 6
print(confirm_length(""))  # Should print 0
