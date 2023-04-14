import PySimpleGUI as gui

# gui imports
import gui_settings
import gui_layouts
import gui_debug
import gui_theme
import gui_prompt_user as prompt
import gui_prompt_user_return as prompt_return
import gui_packer

import directory

import os

def window():

    config = gui_layouts.Layouts()
    
    layout = config.layout_base()

    window = gui.Window("Arma 3 Utilities", layout, icon=f"{os.getcwd()}/crow_1.ico", size=(500, 350), element_justification='c', finalize=True)

    window.set_title("Arma 3 Utilities")

    return window

def event_handlers(window_a):

    while True:
        window, event, values = gui.read_all_windows()

        if (window == window_a and event == gui.WIN_CLOSED):
            break

        match event:
            case gui.WIN_CLOSED:
                window.close()

            #IMAGE TOOLS#

            case "paa_to_png":
                import conversion
                window.perform_long_operation(lambda : conversion.convert_textures("paa", "png"), "converted_textures")

            case "png_to_paa":
                import conversion
                window.perform_long_operation(lambda : conversion.convert_textures("png", "paa"), "converted_textures")

            ##IMAGE TOOLS##

            #PBO TOOLS#

            case "pack_pbo":
                import packer
                window.perform_long_operation(lambda : packer.pack_all_pbo(), "packed_pbo")

            case "pack_pbo_settings":
                gui_packer.window()
                # in_path = directory.grab_directory()

                # out_path = directory.grab_directory()

                # if ((in_path != None) and (out_path != None)):

                #     x = {
                #         "in_path": in_path,
                #         "out_path": out_path,
                #     }

                #     gui_settings.save_to_json(x, "packer")

            case "packer_input":
                data = prompt_return.user_return_folder("Please select an input directory")
                print(data)

                x = {
                    "in_path": data,
                }

                gui_settings.update_to_json(x, "packer")

            case "packer_output":
                data = prompt_return.user_return_folder("Please select an output directory")
                print(data)
            
                x = {
                    "out_path": data,
                }

                gui_settings.update_to_json(x, "packer")
                
            case "key_input":
                data = prompt_return.user_return_file("Please select a key")
                print(data)

                x = {
                    "key_path": data,
                }

                gui_settings.update_to_json(x, "packer")

            ##PBO TOOLS##

            #SETTINGS#

            case "settings":
                gui_settings.window()
                print(str(window))

            case "path_to_tools":
                gui_settings.select_tools()

            case "open_debug_window":
                gui_debug.window()

            case "window_theme":
                theme = values['window_themes']
                # print(theme)
                x = {
                    "theme": theme,
                }

                gui_settings.update_to_json(x, "settings")

                prompt.user("Info", "These settings will be applied when the program next starts.")

            ##SETTINGS##

def window_init():

    if (os.path.isfile(f"{os.getcwd()}/settings.json")):
        print("Settings file found")

        json = gui_settings.read_from_json("settings")

        if "theme" in json:
            print("Theme found")
            gui_theme.change(json["theme"])
        else:
            print("Theme not found, using default")
            
            x = {
                "theme": "Dark",
            }

            gui_settings.update_to_json(x, "settings")

        print("Settings file found")
    else:

        gui_theme.change("Dark")

        x = {
            "init": "active",
        }

        gui_settings.save_to_json(x, "settings")

        gui_settings.select_tools()

    # window_b = gui_debug.window_debug()

    window_a = window()
    event_handlers(window_a)

window_init()