import os
import subprocess
from threading import Thread

import gui_prompt_user
import gui_prompt_user_return
import gui_settings
import gui_threads
import gui_utility
import conversion

def pack_pbo(path, path_in, path_out, path_key, folder):
    isFile = os.path.isfile(f"{folder}")
    notAllowed = ["@", ".git", ".vscode"]
    #reiterate through the notAllowed extensions or keywords, stops things like mod folders being packed
    for folderName in notAllowed:
        if (folderName in str(folder)):
            isFile = True

    if (isFile == False):
        # print(f"There are currently {len(processes)} processes active.")

        # print(f"{path_in}/{folder} was a folder, packing\n\n\n\n\n")
        subprocess.run([f"{path}\AddonBuilder\AddonBuilder.exe", f"{path_in}/{folder}", path_out, "-clear", "-temp", "-binarizeNoLogs", f"-include={os.getcwd()}/include.txt", f"-sign={path_key}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time = gui_utility.get_time()
        print(f"\nFinished packing file {folder} - [{time}]")
        # print(f"-prefix={prefix}\{folder}")
    else:
        print(f"{path_in}/{folder} was not a folder, not packing")

    # if (len(processes) >= 10):
    #     print("Too many processes, throttling")
    #     time.sleep(3.7)
    #     for i in range(5):
    #         processes.pop()

def pack_all_pbo(convert=False):

    tools = gui_settings.read_from_json_return("settings", "tools")

    packer_path = f"{os.getcwd()}/packer.json"

    packer_exists = gui_utility.verify_path(packer_path)

    if (packer_exists):
        gui_utility.new_line()
        # print("Packer settings file found")

        in_path = gui_settings.read_from_json_return("packer", "in_path")

        out_path = gui_settings.read_from_json_return("packer", "out_path")

        key_path = gui_settings.read_from_json_return("packer", "key_path")

        if (in_path == "" or out_path == "" or key_path == ""):
            print("Your directory settings exist, but seem to be corrupt. Try resetting the paths.")
        else:

            directories = os.walk(f"{in_path}")
            dirpath, dirnames, filenames = next(directories)

            threads = []

            # convert = gui_settings.read_from_json_return("packer", "convert_textures")
            # convert = True
            if (convert):
                conversion.convert_textures("png", "paa", in_path=in_path)

            for folder in os.listdir(in_path):

                packer_thread = Thread(target=pack_pbo,args=(tools, in_path, out_path, key_path, folder))
                threads.append(packer_thread)
                # packer_thread.start()

            gui_threads.start_threads(threads)

            time = gui_utility.get_time()
            
            print(f"\nFinished Packing Folders - [{time}]")
    else:
        # gui_prompt_user.user_error(message="You haven't setup your directory settings yet.")
        print("You haven't setup your directory settings yet.")