'''
 * ptd::ui
 * Contains UI-related functionality.
'''

from tkinter import Tk, Label, Button

def cw(wtitle, geo):
    window = Tk()
    window.title(wtitle)
    window.geometry(geo)
    windows[wtitle] = window
    return window

def ct(windowname, geo, text):
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split('x'))
        label = Label(window, text=text)
        label.place(x=x, y=y)
    else:
        print(f"Error: Window '{windowname}' not found.")

def cb(windowname, geo, size, name):
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split(','))
        width, height = map(int, size.split(','))
        button = Button(window, text=name)
        button.place(x=x, y=y, width=width, height=height)
        windows[f"{windowname}_{name}_button"] = button
    else:
        print(f"Error: Window '{windowname}' not found.")
