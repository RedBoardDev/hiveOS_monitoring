import json

def f_get_temp():
    with open("config.json", "r") as file:
        data = json.loads(file.read())
    return (data['temp_max'])

def f_get_memtemp():
    with open("config.json", "r") as file:
        data = json.loads(file.read())
    return (data['memtemp_max'])

def f_get_channel():
    with open("config.json", "r") as file:
        data = json.loads(file.read())
    return (data['channel'])