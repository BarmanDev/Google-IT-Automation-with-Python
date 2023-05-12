import csv
hosts = [["workstation.local", "192.168.25.46"], [
    "webserver.cloud", "10.2.5.6"]]  # -> Datos que queremos almacenar

with open('hosts.csv', 'w') as hosts_csv:  # -> Abrimos el archivo
    writer = csv.writer(hosts_csv)
    writer.writerrows(hosts)

# writerow 1 fila
# writerows todas juntas
# linux escribimos cat. hosts:
