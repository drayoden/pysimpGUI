# hellopsg.py

import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("Demo", layout)

# event loop
while True:
    event, values = window.read()

    # end program if user closes window or
    # presses the OK button

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
