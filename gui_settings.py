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

def save_to_json(data, file_name):

    #y = json.dumps(x)

    with open(f'{os.getcwd()}/{file_name}.json', 'w+') as file:
        json.dump(data, file)

def read_from_json(file_name):
    with open(f'{os.getcwd()}/{file_name}.json', 'r') as file:
        y = json.load(file)

    return y

def select_tools():
    path = directory.grab_directory()

    x = {
        "tools": path,
    }

    save_to_json(x, "settings")