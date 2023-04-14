import os
import subprocess
import time
import json

import directory
import gui_settings
import gui_prompt_user as prompt

tools = gui_settings.read_from_json("settings")

def convert_textures(file_type_from, file_type_to):

    #file_clear = open(f"{os.getcwd()}/textures.txt", "w+")
    #file_clear.close()

    in_path = directory.grab_directory()

    processes = []

    for (dir_path, dir_names, file_names) in os.walk(in_path):

            for file_name in file_names:

                #print(file_name)

                #subfolder = 

                # subfolder = dir_path.split(os.sep)
                subfolder = "NONE"

                # if ("[python]" in str(subfolder)):
                #     subfolder = "IGNORE"

                if (file_name.endswith(f".{file_type_from}")):

                    file_name_dir = f"""----------------------------------------------
Filename: {file_name}\n
Folder: {dir_path}/{file_name[:-4]}.{file_type_from}\n
Subfolder: {subfolder[3]}\n----------------------------------------------"""

                    print(file_name_dir)

                    #file_open = open(f"{os.getcwd()}/textures.txt", "a+")

                    #file_open.write(file_name_dir)

                    try:

                        path = tools["tools"]

                        proc = subprocess.Popen([f"{path}/TexView2/Pal2PacE.exe", f"{dir_path}/{file_name[:-4]}.{file_type_from}", f"{dir_path}/{file_name[:-4]}.{file_type_to}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        # print(f"{dir_path}/{file_name[:-4]}.{file_type_from}")
                        # print(f"{dir_path}/{file_name[:-4]}.{file_type_to}")
                        processes.append(proc)

                        # state = proc.communicate()
                        # print(state)
                        if (len(processes) >= 10):
                            print("Too many processes, throttling")
                            time.sleep(3.7)
                            for i in range(5):
                                processes.pop()

                        print(f"There are currently {len(processes)} processes active.")

                    except:

                        # print("Error: Image Conversion Failed")
                        prompt.user_error("Error", "Image Conversion Failed")

    print(f"Finished converting. Conversion type was {file_type_from} to {file_type_to}")
    # os.system('cls||clear')