import os
import subprocess
import time
import json
from threading import Thread

import directory
import gui_settings
import gui_threads
import gui_prompt_user as prompt

tools = gui_settings.read_from_json("settings")

# def thread_check_loop(threads):
#     time.sleep(1)
#     if (len(threads) >= 10):
#         thread_check_loop(threads)
#     else:
#         return True

def convert_texture(path, dir_path, file_name, file_type_from, file_type_to):
    print(f"Started converting file {file_name} to {file_name[:-4]}.{file_type_to}")

    proc = subprocess.run([f"{path}/TexView2/Pal2PacE.exe", f"{dir_path}/{file_name[:-4]}.{file_type_from}", f"{dir_path}/{file_name[:-4]}.{file_type_to}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    print(f"Finished converting file {file_name} to {file_name[:-4]}.{file_type_to}")

def convert_textures(file_type_from, file_type_to, in_path="default"):

    if (in_path == "default"):
        in_path = directory.grab_directory()

    #file_clear = open(f"{os.getcwd()}/textures.txt", "w+")
    #file_clear.close()

    # in_path = directory.grab_directory()

    threads = []

    for (dir_path, dir_names, file_names) in os.walk(in_path):

            path = tools["tools"]

            for file_name in file_names:

                    try:
                        
                        # if (len(threads) >= 20):
                        #     print("Too many processes, throttling")
                        #     time.sleep(5)
                        print(file_name)
                        print(f".{file_type_from}")

                        if (file_name.endswith(f".{file_type_from}")):

                            conversion_thread = Thread(target=convert_texture,args=(path, dir_path, file_name, file_type_from, file_type_to))
                            threads.append(conversion_thread)
                        # conversion_thread.start()

                        # print(f"There are currently {len(processes)} processes active.")

                    except:

                        # print("Error: Image Conversion Failed")
                        prompt.user_error("Error", "Image Conversion Failed")
                        
    gui_threads.start_threads(threads)

    print(f"Finished converting. Conversion type was {file_type_from} to {file_type_to}")
    # os.system('cls||clear')