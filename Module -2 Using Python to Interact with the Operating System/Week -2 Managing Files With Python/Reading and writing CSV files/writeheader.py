import csv
# Creamos el dicionario con los datos que queremos
users = [{"name": "Sol Mansi", "username": "solm", "department": "ItInfrastructure"},
         {"name": "Lio Nelson", "username": "lion",
             "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
# Almacenamos las claves que queremos escribir en el archivo csv
keys = ["name", "username", "department"]
# Abrimos el archivo
with open('y_deparment.csv', 'w') as by_department:
    # Creamos el 'DicWriter' pasando las claves que escribimos
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()  # -> Crea la primera linea basado en las claves
    # -> Convierte el dicionario en lineas en el archivo
    writer.writerows(users)
