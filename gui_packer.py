import PySimpleGUI as gui
import os
import gui_layouts

def window():

    config = gui_layouts.Layouts()

    layout = config.layout_packer_settings()

    # print(layout)

    window_debug = gui.Window("Packer Settings", layout, size=(500, 350), icon=f"{os.getcwd()}/crow_1.ico", element_justification='c', finalize=True)

    # window_debug.disappear()