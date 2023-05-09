x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

print("jpg" in file_counts)  # -> true
print("html" in file_counts)  # -> true

file_counts["csv"] = 17
print(file_counts)

del file_counts["jpg"]
print(file_counts)
