import re
result = re.search(r"aza", "Plaza")
print(result)

print(re.search(r"^x", "xenon"))
print(re.search("p.ng", "penguin"))

# <re.Match object; span=(0, 1), match='x'>   -> el span es la posicion 1  y donde termina

# Ignorando mayusculas y minuscolas

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
