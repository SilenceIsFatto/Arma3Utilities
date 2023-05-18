import PySimpleGUI as gui
import os

def user_return_file(message, default_path="default", file_types=(("All Files", ". *"))):

    if (default_path == "default"):
        default_path = os.getcwd()

    data = gui.popup_get_file(message, default_path=default_path)

    if (data == None):
        data = default_path

    return data

def user_return_folder(message, default_path="default"):

    if (default_path == "default"):
        default_path = os.getcwd()

    data = gui.popup_get_folder(message, default_path=default_path)

    if (data == None):
        data = default_path

    return data

def user_return(message):

    data = gui.popup_get_text(message)

    return data