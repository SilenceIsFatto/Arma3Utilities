import  tkinter as tk
from tkinter import filedialog

def grab_directory():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()

    if (file_path == ""):
        file_path = grab_directory()

    return file_path