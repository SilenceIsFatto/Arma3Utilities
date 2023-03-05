import PySimpleGUI as gui

def prompt_user_return(message):

    data = gui.popup_get_text(message)

    return data