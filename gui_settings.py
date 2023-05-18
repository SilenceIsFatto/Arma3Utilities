import PySimpleGUI as gui
import json
import os
import directory

import gui_layouts
import gui_debug
import gui_prompt_user as prompt
import gui_prompt_user_return as prompt_return

def window():

    config = gui_layouts.Layouts()
    
    layout = config.layout_settings()

    window = gui.Window("Arma 3 Utility Settings", layout, icon=f"{os.getcwd()}/crow_1.ico", size=(400, 300), element_justification='c', finalize=True)

    # window.bring_to_front()

    #size=(400,400)

    return window

def save_to_json(data, file_name):

    #y = json.dumps(x)

    with open(f'{os.getcwd()}/{file_name}.json', 'w+') as file:
        json.dump(data, file, indent=4)

def read_from_json(file_name):
    with open(f'{os.getcwd()}/{file_name}.json', 'r') as file:
        y = json.load(file)

    return y

def read_from_json_return(file_name, data):
    print(file_name)
    if ("/" in file_name):
        
        with open(f'{file_name}', 'r') as file:
            x = json.load(file)

    else:

        with open(f'{os.getcwd()}/{file_name}.json', 'r') as file:
            x = json.load(file)

    y = x[data]

    return y

def update_to_json(data, file_name):

    try:

        with open(f'{os.getcwd()}/{file_name}.json', 'r') as file:
            y = json.load(file)

        y.update(data)
        
        print(y)

        save_to_json(y, file_name)

    except:
        # print("Something went wrong with initialization. Some things may still work.")
        prompt.user_error("Error", "Something went wrong whilst saving settings. Some things may still work. Try creating an empty packer.json file")
        

def select_tools():
    # prompt.user("Info", "Please select your Arma 3 Tools root directory.")

    # path = directory.grab_directory()

    # if (os.path.isfile(f"{os.getcwd()}/settings.json")):
    #     tools = read_from_json("settings")
    #     tools_path = tools["tools"]
    # else:
    #     tools_path = ""

    path = prompt_return.user_return_folder("Please select your Arma 3 Tools directory", default_path="")

    # if (path != None):

    x = {
        "tools": path,
    }

    update_to_json(x, "settings")