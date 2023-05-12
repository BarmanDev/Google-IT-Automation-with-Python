# linux

# cat csv_file.txt -> ver el contenido del archivo en la termial linux

import csv
f = open("csv_file.txt")  # abrimos el archivo
# -> creamos un objeto reader para poder abrir el archivo en modo lectura
csv_f = csv.reader(f)

# Recorremos cada fila del archivo CSV utilizando el objeto de arriba
for row in csv_f:
    # -> Asigna los valores de los campos de la fila actial a la variables
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(
        name, phone, role))  # -> Imprimimos la información

f.close()  # -> Cerramos el archivo
