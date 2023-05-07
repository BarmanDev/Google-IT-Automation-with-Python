class Apple:
    def __init__(self, color, flavor):  # Constructor
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = Apple("red", "sweet")  # Constructor
print(jonagold.color)
print(jonagold)

help(Apple)
