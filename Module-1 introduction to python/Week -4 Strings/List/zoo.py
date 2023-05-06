animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Averange length: {}".format(chars, chars/len(animals)))
