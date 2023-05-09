file = open("spider.txt")
print(file.readline())  # -> lee la primera liena

print(file.read())  # ->lee todo el fichero

file.close()  # -> cierra el archivo importante cerrarlos siempre para tener un menor consumo de recursos y posibles problemas

# Python cerrara el archivo automaticamente
with open("spider.txt") as file:
    print(file.readline())
