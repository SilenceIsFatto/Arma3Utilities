import PySimpleGUI as gui
import gui_layouts

def window():

    config = gui_layouts.Layouts()

    layout = config.layout_console()

    window = gui.Window("Debug Window", layout, size=(600, 300), element_justification='c', finalize=True)

    # window.disappear()