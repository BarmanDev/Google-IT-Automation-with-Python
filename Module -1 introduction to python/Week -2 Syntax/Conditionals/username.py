def hint_username(username):
    if len(username) < 3:
        print("invalid username. Must be at least 3 charcters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Value username")
