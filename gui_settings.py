import json
import os
import directory

def save_to_json(data):
    x = {
        "tools": data[0],
    }

    #y = json.dumps(x)

    with open(f'{os.getcwd()}/settings.json', 'w+') as file:
        json.dump(x, file)

def read_from_json():
    with open(f'{os.getcwd()}/settings.json', 'r') as file:
        y = json.load(file)

    return y

def select_tools():
    path = directory.grab_directory()

    save_to_json([path])