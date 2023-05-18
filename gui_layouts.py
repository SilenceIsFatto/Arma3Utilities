import PySimpleGUI as gui

import gui_settings

class Layouts:

    def __init__(self):
        print("Running")

    def layout_console(self):
        frame_layout = [[gui.Multiline("", size=(80, 20), autoscroll=True, reroute_stdout=True, reroute_stderr=True, key='console_output')]]

        layout = [
            [gui.Frame("Output console", frame_layout)]
        ]

        return layout

    def layout_settings(self):

        themes = [
            "Dark",
            "DarkAmber",
            "DarkGrey8",
            "Dark2",
            "SystemDefault",
            "Reddit",
            "Black"
        ]

        json = gui_settings.read_from_json("settings")

        if "theme" in json:
            cur_theme = json["theme"]
        else:
            cur_theme = themes[0]

        layout = [
            [gui.Text("Settings")],

            [gui.Button("Path To Arma 3 Tools", pad=(0,10), key="path_to_tools")],

            [gui.Button("Open Debug Window", pad=(0,10), key="open_debug_window")],

            [gui.Combo(themes, cur_theme, font=('Arial Bold', 10), enable_events=True, readonly=True, key='window_themes')],

            [gui.Button("Set Theme", pad=(0,10), key="window_theme")],
        ]

        return layout

    def layout_packer_settings(self):

        # json = gui_settings.read_from_json("settings")

        # if "theme" in json:
        #     cur_theme = json["theme"]
        # else:
        #     cur_theme = themes[0]

        layout = [
            [gui.Text("Packer Settings")],

            [gui.Button("Input Directory", pad=(0,10), key="packer_input")],

            [gui.Button("Output Directory", pad=(0,10), key="packer_output")],

            [gui.Button("Key Directory", pad=(0,10), key="key_input")],

            [gui.Button("Save", pad=(0,10), key="packer_settings_save")],

            [gui.Button("Load", pad=(0,0), key="packer_settings_load")],
        ]

        return layout
    
    def layout_base(self):

        layout = [
            [gui.Text("Image Tools")],

            #background_color="GRAY"
            #visible=False

            # [gui.Text('1', enable_events=True,
            # key='-TEXT-', font=('Arial Bold', 10),
            # size=(15), relief="raised", border_width=3,
            # expand_x=False, justification='center')],

            #[gui.Button("...", pad=(0,0), size=(1,1), key="-CPI-")],

            [gui.Button("PAA > PNG Mass Conversion", pad=(0,10), key="paa_to_png")],
            
            [gui.Button("PNG > PAA Mass Conversion", pad=(0,0), key="png_to_paa")],

            [gui.Text("PBO Tools", pad=(0,20))],

            [gui.Button("Pack Directory", pad=(0,0), key="pack_pbo")],
            
            [gui.Button("Directory Settings", pad=(0,0), key="pack_pbo_settings")],

            [gui.Button("Settings", pad=(10,55), key="settings")],
        ]

        return layout