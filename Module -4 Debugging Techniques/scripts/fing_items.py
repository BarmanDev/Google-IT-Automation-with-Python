"""
Pregunta 2
The find_item function uses binary search to recursively locate an item in the list, returning True if found, False otherwise. 
Something is missing from this function. Can you spot what it is and fix it? Add debug lines where appropriate, to help narrow down the problem.

"""


def find_item(lst, item):
    # Returns True if the item is in the list, False if not.
    if len(lst) == 0:
        return False

    # Is the item in the center of the list?
    middle = len(lst) // 2
    if lst[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item < lst[middle]:
        # Call the function with the first half of the list
        print("Checking first half:", lst[:middle])  # Debug line
        return find_item(lst[:middle], item)
    else:
        # Call the function with the second half of the list
        print("Checking second half:", lst[middle+1:])  # Debug line
        return find_item(lst[middle+1:], item)

    # Item not found
    return False


# Do not edit below this line - This code helps check your work!
list_of_names = ["Alex", "Cameron", "Chris", "Drew",
                 "Jamie", "Jordan", "Logan", "Parker", "Terry", "Taylor"]
# The list_of_names must be sorted for binary search to work correctly

print(find_item(list_of_names, "Alex"))   # True
print(find_item(list_of_names, "Andrew"))  # False
print(find_item(list_of_names, "Drew"))   # True
print(find_item(list_of_names, "Jared"))  # False
