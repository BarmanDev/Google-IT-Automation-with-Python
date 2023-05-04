"""
Pregunta 4
Fill in the blanks to complete the “multiplication_table” function. This function should print a multiplication 
table, where each number is the result of multiplying the first number of its row by the number at the top of its column. 
Complete the range sequences in the nested loops so that “multiplication_table(1, 3)” will print:

1 2 3

2 4 6

3 6 9
"""


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop + 1):
        # Complete the inner loop range
        for y in range(start, stop + 1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
