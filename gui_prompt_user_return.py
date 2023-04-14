import PySimpleGUI as gui

def user_return_file(message):

    data = gui.popup_get_file(message)

    return data

def user_return_folder(message):

    data = gui.popup_get_folder(message)

    return data

def user_return(message):

    data = gui.popup_get_text(message)

    return data