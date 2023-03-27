import PySimpleGUI as gui

def change(theme):

    gui.theme(theme)

    print(f"Theme was set to {theme}")