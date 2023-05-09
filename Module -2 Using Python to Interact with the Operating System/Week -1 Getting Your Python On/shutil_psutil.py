"""
En linux sería así:

import shutil

du = shutil.disk_usage("/")
print (du.free/du.total*100)

"""

import psutil
du = psutil.disk_usage("C:\\")  # Replace C:\\ replace by drive letter
free_percent = du.free / du.total * 100
free_percent_rounded = round(free_percent, 2)
print("Tienes un ", free_percent_rounded, "% libre de espacio en el disco")


print("Tines un uso de cpu de ", psutil.cpu_percent(0.1), "%")
