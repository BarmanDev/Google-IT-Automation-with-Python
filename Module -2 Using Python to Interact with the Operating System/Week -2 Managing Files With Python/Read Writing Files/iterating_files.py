# Imprime el documento en mayusculas
with open("spider.txt") as file:
    for line in file:
        print(line.upper())


# Los saltos de linea crean un espacio, para evitarlo usamos line.strip()
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
