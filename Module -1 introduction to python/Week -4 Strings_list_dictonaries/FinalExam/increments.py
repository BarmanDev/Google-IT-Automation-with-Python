"""
Fill in the blank to complete the “increments” function. 
This function should use a list comprehension to create a list of numbers incremented by 2 (n+2).
 The function receives two variables and should return a list of incremented consecutive numbers
between “start” and “end” inclusively (meaning the range should include both the “start” and “end”
 values). Complete the list comprehension in this function so that input like “squares(2, 3)”
   will produce the output “[4, 5]”.
"""


def increments(start, end):
    # Create the required list comprehension.
    return [num + 2 for num in range(start, end+1)]


print(increments(2, 3))  # Should print [4, 5]
print(increments(1, 5))  # Should print [3, 4, 5, 6, 7]
print(increments(0, 10))  # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
