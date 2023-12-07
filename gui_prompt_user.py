import PySimpleGUI as gui

def user(title, message):

    gui.popup(title, message)

def user_error(title, message):

    gui.popup_error(title, message)