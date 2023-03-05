import PySimpleGUI as gui
import json
import os
import directory

import gui_layouts
import gui_debug

def window_settings():

    config = gui_layouts.Layouts()
    
    layout_setting = config.layout_settings()

    window_setting = gui.Window("Arma 3 Utility Settings", layout_setting, size=(400, 300), element_justification='c', finalize=True)

    # window.bring_to_front()

    #size=(400,400)

    return window_setting

def window_settings_init():

    window_c = window_settings()

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