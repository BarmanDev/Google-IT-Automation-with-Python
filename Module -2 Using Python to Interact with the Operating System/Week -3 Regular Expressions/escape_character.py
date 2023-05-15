import re
print(re.search(r"\.com", "mydomain.com"))
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))


pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "my_variable1"))
