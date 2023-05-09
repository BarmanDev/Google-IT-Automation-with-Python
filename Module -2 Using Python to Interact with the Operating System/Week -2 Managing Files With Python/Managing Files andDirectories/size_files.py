import os
import datetime
txt = open("holaCaracola.txt", "w")  # -> creamos el archivo
txt.write("Hola caracola")
txt.write("Soy un archivo de prueba :) ")
txt.close()

size = os.path.getsize("holaCaracola.txt")
# -> 1683640645.9168618 cuenta los segundos desde el 1 de enero de 1970
timestamp = os.path.getatime("holaCaracola.txt")
# -> Con esta función lo pasamos a tiempo que entendemos :)
time = datetime.datetime.fromtimestamp(timestamp)

path = os.path.abspath("holaCaracola.txt")


print("el archivo tiene un tamaño de: ", size)
print("el archivo fue creado el: ", time)
print("el archivo esta en: " + path)
