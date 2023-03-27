import  tkinter as tk
from tkinter import filedialog

import sys
import gui_prompt_user as gui

def grab_directory():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()

    if (file_path == ""):
        print("Path not entered, aborting")
        # file_path = grab_directory()
        # gui.prompt_user("Oops!", "You didn't select a directory.")
        # sys.exit()
    else:
        return file_path