# Escribimos el nombre de las reservas en un fichero de texto
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

# Leemos el contenido por consola
with open("guests.txt") as guests:
    for line in guests:
        print(line)
# Agregamos 3 reservas nuevas
new_guests = ["Sam", "Danielle", "Jacob"]


# Abirmos el archivo y añadimos las nuevas reservas
with open("guests.txt", "w") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# Vemos de nuevo las reservas
with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Registramos las salidas
checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

# Agregamos la lista temporal elimando los espacios en blanco
with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

# Eliminamos los nombres de la lista check-out
with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# Vemos de nuevo las reservas
with open("guests.txt") as guests:
    for line in guests:
        print(line)


# Verificamos si Bob y Andrea han hecho check-in
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))
