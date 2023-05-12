import os

# Linux

# Imprime la ruta
print(os.getcwd())
# Crear carpeta
os.mkdir("new_dir")
# Moverse a una carpeta
os.chdir("new_dir")
# Eliminar una carpeta
os.rmdir("new_dir")
# Ver el contenido de una carpeta
# -> Devuelve una lista no sabemos que tipo de archivos son
os.listdir("website")

# Está función delviele el tipo de archivo que es
dir = "website"
for name in os.listdir(dir):
    # os.path.join cambia \ a / para que funcione en linux
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory" .format(fullname))
else:
    print("{} is a file".format(fullname))
