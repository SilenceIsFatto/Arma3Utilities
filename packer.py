import os
import subprocess
import time

import directory
import gui_settings

def pack_all_pbo():

    tools = gui_settings.read_from_json("settings")

    if (os.path.isfile(f"{os.getcwd()}/packer.json")):
        print("Packer settings file found")

        in_path = gui_settings.read_from_json("packer")

        out_path = gui_settings.read_from_json("packer")
    else:
        in_path = directory.grab_directory()

        out_path = directory.grab_directory()

        x = {
            "in_path": in_path,
            "out_path": out_path,
        }

        gui_settings.save_to_json(x, "packer")

    path = tools["tools"]
    path_in = in_path["in_path"]
    path_out = out_path["out_path"]

    directories = os.walk(f"{path_in}")
    dirpath, dirnames, filenames = next(directories)

    processes = []

    for folder in os.listdir(path_in):
        isFile = os.path.isfile(f"{folder}")
        notAllowed = ["@", ".git", ".vscode"]
        #reiterate through the notAllowed extensions or keywords, stops things like mod folders being packed
        for folderName in notAllowed:
            if (folderName in str(folder)):
                isFile = True

        if (isFile == False):
            print((path_in, path_out))

            print(f"\033[1;32m{path_in}/{folder} was a folder, packing\n\n\n\n\n")
            subprocess.Popen([f"{path}\AddonBuilder\AddonBuilder.exe", f"{path_in}/{folder}", path_out, "-clear", "-temp", "-binarizeNoLogs", f"-include={os.getcwd()}/include.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # use the include.txt
        else:
            print(f"{path_in}/{folder} was not a folder, not packing\n\n\n\n\n")

        if (len(processes) >= 10):
            print("Too many processes, throttling")
            time.sleep(3.7)
            for i in range(5):
                processes.pop()

        print(f"There are currently {len(processes)} processes active.")