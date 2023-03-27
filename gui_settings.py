import PySimpleGUI as gui
import json
import os
import directory

import gui_layouts
import gui_debug
import gui_prompt_user

def window_settings():

    config = gui_layouts.Layouts()
    
    layout_setting = config.layout_settings()

    window_setting = gui.Window("Arma 3 Utility Settings", layout_setting, icon=f"{os.getcwd()}/crow_1.ico", size=(400, 300), element_justification='c', finalize=True)

    # window.bring_to_front()

    #size=(400,400)

    return window_setting

def window_settings_init():

    window_c = window_settings()

def save_to_json(data, file_name):

    #y = json.dumps(x)

    with open(f'{os.getcwd()}/{file_name}.json', 'w+') as file:
        json.dump(data, file, indent=4)

def read_from_json(file_name):
    with open(f'{os.getcwd()}/{file_name}.json', 'r') as file:
        y = json.load(file)

    return y

def update_to_json(data, file_name):

    try:

        with open(f'{os.getcwd()}/{file_name}.json', 'r') as file:
            y = json.load(file)

        y.update(data)
        
        print(y)

        save_to_json(y, file_name)

    except:
        print("Something went wrong with initialization. Some things may still work.")

def select_tools():
    gui_prompt_user.prompt_user("Info", "Please select your Arma 3 Tools root directory.")

    path = directory.grab_directory()

    if (path != None):

        x = {
            "tools": path,
        }

        update_to_json(x, "settings")