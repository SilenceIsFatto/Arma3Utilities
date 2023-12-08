import os
import subprocess
from threading import Thread

import gui_utility
import gui_settings
import gui_threads
import gui_prompt_user as prompt
import gui_prompt_user_return as prompt_return

tools = gui_settings.read_from_json_return("settings", "tools")

def convert_texture(path, dir_path, file_name, file_type_from, file_type_to, threads):
    # print(f"Started converting file {file_name} to {file_name[:-4]}.{file_type_to}")

    proc = subprocess.run([f"{path}/TexView2/Pal2PacE.exe", f"{dir_path}/{file_name[:-4]}.{file_type_from}", f"{dir_path}/{file_name[:-4]}.{file_type_to}"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    time = gui_utility.get_time()
    print(f"Finished converting file {file_name} to {file_name[:-4]}.{file_type_to} - [{time}]")

    if (len(threads) != 1):

        threads.pop(1)

    # print(len(threads))

def convert_textures(file_type_from, file_type_to, in_path="default"):

    gui_utility.new_line()

    if (in_path == "default"):
        in_path = prompt_return.user_return_folder("Select a path for conversion (includes subfolders)")

    threads = []

    for (dir_path, dir_names, file_names) in os.walk(in_path):

            for file_name in file_names:

                    try:

                        # print(len(threads))
                        
                        # while (len(threads)) != 20:

                        # if (len(threads) >= 10):
                        #     time.sleep(1)

                        if (file_name.endswith(f".{file_type_from}")):

                            conversion_thread = Thread(target=convert_texture,args=(tools, dir_path, file_name, file_type_from, file_type_to, threads))
                            threads.append(conversion_thread)

                    except:

                        prompt.user_error("Error", "Image Conversion Failed")
                        
    gui_threads.start_threads(threads)

    time = gui_utility.get_time()
    print(f"\nFinished converting images. Conversion type was {file_type_from} to {file_type_to} - [{time}]\n")
    # os.system('cls||clear')