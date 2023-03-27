import PySimpleGUI as gui
import gui_layouts

def window_debug():

    config = gui_layouts.Layouts()

    layout_debug = config.layout_console()

    # print(layout)

    window_debug = gui.Window("Debug Window", layout_debug, size=(600, 300), element_justification='c', finalize=True)

    # window_debug.disappear()