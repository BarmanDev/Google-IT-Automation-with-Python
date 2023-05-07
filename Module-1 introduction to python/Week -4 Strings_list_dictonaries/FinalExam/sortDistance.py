"""
Pregunta 3
Consider the following scenario about using Python lists: 

Employees at a company shared  the distance they drive to work (in miles) through an online survey. These distances were automatically added by Python to a list called “distances” in the order that each employee submitted their distance. Management wants the list to be sorted in the order of the longest distance to the shortest distance. 

Complete the function to sort the “distances” list. This function should:

sort the given “distances” list, passed through the function’s parameters; ; 

reverse the sort order so that it goes from the longest to the shortest distance;

return the modified “distances” list.
"""


def sort_distance(distances):
    distances.sort()  # Sort the list
    distances.reverse()  # Reverse the order of the list
    return distances


print(sort_distance([2, 4, 0, 15, 8, 9]))
# Should print [15, 9, 8, 4, 2, 0]
