import  tkinter
from tkinter import filedialog

import PySimpleGUI as gui

import gui_prompt_user
import gui_utility
import os

def user_return(message):

    data = gui.popup_get_text(message)

    return data

def user_return_file(message, default_path="default", file_required=False, file_types=(("All Files", ".*"))):

    default_path = gui_utility.get_default_path(default_path)

    filename = filedialog.askopenfilename(title=message, initialdir=default_path, filetypes=[(file_types[0], file_types[1])])

    if (file_required and len(filename) == 0):
        gui_prompt_user.user_error("Error!", "You didn't select a file, however one is required. Things may not work correctly!")
        user_return_file(message, default_path, file_required, file_types)

    return filename

def user_return_folder(message, default_path="default", file_required=False):

    default_path = gui_utility.get_default_path(default_path)

    directory = filedialog.askdirectory(mustexist=True, title=message, initialdir=default_path)

    if (file_required and len(directory) == 0):
        gui_prompt_user.user_error("Error!", "You didn't select a folder, however one is required. Things may not work correctly!")
        directory = user_return_folder(message, default_path, file_required)

    return directory