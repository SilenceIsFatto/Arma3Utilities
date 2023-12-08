import PySimpleGUI as gui

def user(title, message):

    gui.popup(title, message)

def user_error(title="Error", message="Something Went Wrong!"):

    gui.popup_error(title, message)