# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1,
# element2, element3".
def list_elements(list_name, elements):

    # This task can be completed in a single line of code. The
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(list_elements("Printers", ["Color Printer",
      "Black and White Printer", "3-D Printer"]))
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"
