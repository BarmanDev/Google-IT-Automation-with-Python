fullname = ('Borja', 'Fernandez', 'Gaitero')
print(fullname)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    rematign_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, rematign_seconds


result = convert_seconds(5000)
type(result)  # -> Tuple
print(result)

hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
