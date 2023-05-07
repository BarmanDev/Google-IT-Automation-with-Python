"""
Consider the following scenario about using Python dictionaries: 

Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests each friend will be bringing. 

Complete the function so that the “check_guests” function retrieves the number of guests (value)  the specified friend “guest” (key) is bringing. This function should:

accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;

print the values associated with the key variable.
"""


def check_guests(guest_list, guest):
    return guest_list.get(guest)  # Return the value for the given key


guest_list = {"Adam": 3, "Camila": 3, "David": 5, "Jamal": 3,
              "Charley": 2, "Titus": 1, "Raj": 6, "Noemi": 1, "Sakira": 3, "Chidi": 5}


print(check_guests(guest_list, "Adam"))  # Should print 3
print(check_guests(guest_list, "Sakira"))  # Should print 3
print(check_guests(guest_list, "Charley"))  # Should print 2
