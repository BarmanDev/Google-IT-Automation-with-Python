import csv
# -> Abrimos el archivo y lo asignamos a la variable software
with open('software.csv') as software:
    reader = csv.DictReader(software)  # -> Leemos el archivo
    for row in reader:
        # -> Imprimios en un dicionario
        print(("{} has {} users").format(row["name"], row["users"]))
