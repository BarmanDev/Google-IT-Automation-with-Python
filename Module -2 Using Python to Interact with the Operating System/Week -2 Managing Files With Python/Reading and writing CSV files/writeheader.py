import csv
users = [{"name": "Sol Mansi", "username": "solm", "department": "ItInfrastructure"},
         {"name": "Lio Nelson", "username": "lion",
             "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]
with open('y_deparment.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
