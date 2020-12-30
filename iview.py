# iview.py

# Can only display PNG and GIF
# If you want to support TIFF, JPG and BMP
# use Pillow. Check the PySimpleGUI github
# page for the process

import PySimpleGUI as sg
import os.path

# set window layout for two columns

# left column -- 
file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=[], enable_events=True, size=(40,20), key="-FILE LIST-")
    ],
]

# right column --
image_viewer_column = [
    [sg.Text("Choose an image from the list on left")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# layout --
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED: 
        break

# folder event --
if event == "-FOLDER-":
    folder = values["-FOLDER-"]
    
    try:
        # get list of files
        file_list = os.listdir(folder)
    except: 
        file_list = []
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".png", ".gif"))
    ]

    window["-FILE LIST-"].update(fnames)

# file list event --
elif event == "-FILE LIST-":
    try:
        filename = os.path.join(values["-FILE LIST-"][0])
        window["-TOUT-"].update(filename)
        window["-IMAGE-"].update(filename=filename)
    except:
        pass


window.close()