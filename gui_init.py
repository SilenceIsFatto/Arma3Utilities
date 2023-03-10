import PySimpleGUI as gui
import gui_settings
import gui_layouts
import os
import threading
#import threads

def set_theme(theme):

    gui.theme(theme)

    print(f"Theme was set to {theme}")

def prompt_user_return(message):

    data = gui.popup_get_text(message)

    return data

def prompt_user(title, message):

    gui.popup(title, message)

def prompt_debug():

    gui.show_debugger_window(location=(10,0))

    gui.Print('Re-routing data to this console', do_not_reroute_stdout=False)

    print = gui.Print

set_theme("Dark")

def window_debug():

    config = gui_layouts.Layouts()

    layout_debug = config.layout_console()

    # print(layout)

    window_debug = gui.Window("Debug Window", layout_debug, size=(600, 300), element_justification='c', finalize=True)

def window():

    config = gui_layouts.Layouts()
    
    layout = config.layout_base()

    window = gui.Window("Arma 3 Utilities", layout, size=(400, 300), element_justification='c', finalize=True)

    # window.bring_to_front()

    #size=(400,400)

    return window

# def handle_event(event):
#     match event:
#         case "":

def event_handlers(window):

    while True:
        event, values = window.read(timeout=100)
        # End program if user closes window or
        # presses the OK button

        match event:
            case "paa_to_png":
                import conversion
                # threads.start_thread(conversion.convert_textures("paa", "png"), 10)
                window.perform_long_operation(lambda : conversion.convert_textures("paa", "png"), "Converted Textures")

            case "png_to_paa":
                import conversion
                # threads.start_thread(conversion.convert_textures("paa", "png"), 10)
                window.perform_long_operation(lambda : conversion.convert_textures("png", "paa"), "Converted Textures")

            case "settings":
                gui_settings.select_tools()

            case gui.WIN_CLOSED:
                break

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

    window_b = window_debug()

    window_a = window()
    event_handlers(window_a)

# threads.start_thread(window_init, 1)

window_init()

#window.close()