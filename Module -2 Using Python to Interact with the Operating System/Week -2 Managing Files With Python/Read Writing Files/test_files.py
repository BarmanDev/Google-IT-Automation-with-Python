file = open("spider.txt")  # -> Almacenamos para abrir el archivo
lines = file.readlines()  # ->leemos el contenido del archivo y lo almacenamos en lines
file.close()  # -> Cerramos el archvio
lines.sort()  # -> Ordena las en orden alfabetico ascendente
print(lines)

# Nota: Para archivos muy grandes es más eficiente leer linea por linea
