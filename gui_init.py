import PySimpleGUI as gui

# gui imports
import gui_settings
import gui_layouts
import gui_debug

import directory

import os

def set_theme(theme):

    gui.theme(theme)

    print(f"Theme was set to {theme}")

def prompt_debug():

    gui.show_debugger_window(location=(10,0))

    gui.Print('Re-routing data to this console', do_not_reroute_stdout=False)

    print = gui.Print

set_theme("Dark")

def window():

    config = gui_layouts.Layouts()
    
    layout = config.layout_base()

    window = gui.Window("Arma 3 Utilities", layout, size=(500, 350), element_justification='c', finalize=True)

    # window.bring_to_front()

    #size=(400,400)

    return window

# def handle_event(event):
#     match event:
#         case "":

def event_handlers(window_a):

    while True:
        window, event, values = gui.read_all_windows()

        # print(window)
        # End program if user closes window or
        # presses the OK button

        if (window == window_a and event == gui.WIN_CLOSED):
            break

        match event:
            case gui.WIN_CLOSED:
                window.close()

            case "paa_to_png":
                import conversion
                # threads.start_thread(conversion.convert_textures("paa", "png"), 10)
                window.perform_long_operation(lambda : conversion.convert_textures("paa", "png"), "converted_textures")

            case "png_to_paa":
                import conversion
                # threads.start_thread(conversion.convert_textures("paa", "png"), 10)
                window.perform_long_operation(lambda : conversion.convert_textures("png", "paa"), "converted_textures")

            case "pack_pbo":
                import packer
                window.perform_long_operation(lambda : packer.pack_all_pbo(), "packed_pbo")

            case "pack_pbo_settings":
                in_path = directory.grab_directory()

                out_path = directory.grab_directory()

                x = {
                    "in_path": in_path,
                    "out_path": out_path,
                }

                gui_settings.save_to_json(x, "packer")

            case "settings":
                gui_settings.window_settings_init()
                print(str(window))

            case "path_to_tools":
                select_tools()

            case "open_debug_window":
                gui_debug.window_debug()

        # if event == "Close":
        #     break

        # if event == "paa_to_png":
        #     import conversion
        #     # threads.start_thread(conversion.convert_textures("paa", "png"), 10)
        #     window.perform_long_operation(lambda : conversion.convert_textures("paa", "png"), "Converted Textures")

        # if event == "png_to_paa":
        #     import conversion
        #     # threads.start_thread(conversion.convert_textures("png", "paa"), 10)
        #     window.perform_long_operation(lambda : conversion.convert_textures("png", "paa"), "Converted Textures")

        # if event == "settings":
        #     gui_settings.select_tools()

        # if event == '-CPI-':
        #     try:
        #         data = prompt_user_return("Select clicks per interval")
                
        #         if (data.isdigit() == False):
        #             prompt_user("An error has occured.", f"The input given is not a number.")
        #             break

        #         print(data)
        #         window['-TEXT-'].update(data, font=('Arial Bold', 10))
        #         window['-SL-'].update(data)
        #     except:
        #         prompt_user("An error has occured.", f"Event {event} went wrong.")
        #         print("An error has occured with popup text")

#prompt_user("An error has occured.", f"fat")

def window_init():

    if (os.path.isfile(f"{os.getcwd()}/settings.json")):
        print("Settings file found")
    else:
        gui_settings.select_tools()

    # prompt_debug()

    window_b = gui_debug.window_debug()

    window_a = window()
    event_handlers(window_a)

# threads.start_thread(window_init, 1)

window_init()

#window.close()