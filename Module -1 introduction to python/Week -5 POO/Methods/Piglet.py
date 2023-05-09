class Piglet:
    name = "piglet"

    def speak(self):
        print("Oink! I'm {}! oink!" .format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
