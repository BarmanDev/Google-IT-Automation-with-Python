"""Este programa es un registro de los eventos de inicio y cierre de sesión de diferentes máquinas y usuarios"""

# Clase evento


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# Funciones


def getEventDate(event):
    return event.date

# Función que ordena la lista en un dicionario con key la máquina y como valor los usuarios


def currentUsers(events):
    events.sort(key=getEventDate)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            # Use discard() instead of remove()
            machines[event.machine].discard(event.user)
    return machines


# Función que genera el reporte
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


# Eventos
events = [
    Event('2023-01-21 12:45:56', 'login', 'myworkstation.local', 'Borja'),
    Event('2023-01-22 15:55:26', 'logout', 'webserver.local', 'Borja'),
    Event('2023-01-21 17:25:26', 'login', 'myworkstation.local', 'Bea'),
    Event('2023-01-21 07:20:06', 'logout', 'myworkstation.local', 'Borja'),
    Event('2023-01-21 08:15:56', 'login', 'webserver.local', 'Borja'),
    Event('2023-01-21 11:23:26', 'login', 'mailserver.local', 'Manuel'),

]
# Imprime un lista con los usuarios
users = currentUsers(events)
print(users)

# Genera el informe
generate_report(users)
