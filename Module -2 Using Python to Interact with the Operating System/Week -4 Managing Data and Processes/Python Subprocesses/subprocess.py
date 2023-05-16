# Solo Python 3.7 o inferior
import subprocess
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

print(result.returncode)
