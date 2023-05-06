name = "Borja"
print(name[1])  # -> o
print(name[0])  # -> B
print(name[-1])  # -> a

color = "Orange"
print(color[1:4])  # -> ran

fruit = "Pineapple"
print(fruit[:4])  # -> Pine
print(fruit[4:])  # -> apple

# method index
pets = "Cats & Dogs"
print(pets.index("&"))  # -> 5
print(pets.index("C"))  # -> 0

print("Cats" in pets)  # -> True
print("Dragons" in pets)  # -> False
