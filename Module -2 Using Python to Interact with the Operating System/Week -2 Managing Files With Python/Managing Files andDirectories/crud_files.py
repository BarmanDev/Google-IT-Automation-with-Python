import os

txt = open("delete.txt", "w")  # -> creamos el archivo
txt.write("Hola caracola")
txt.write("Soy un archivo de prueba :) ")
txt.write("Estoy triste porque me van a destruir :(")
txt.close()

os.rename("delete.txt", "bye.txt")  # -> Renombramos con lo queamos
os.remove("bye.txt")  # Eliminamos

# Vemos si el archivo existe o no (TRUE FALSE)
test = os.path.exists("bye.txt")
print("¿El archivo existe?", test)
