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

def bc(name, code):
    for key, button in windows.items():
        if key.endswith(f"_{name}_button"):
            def on_click():
                for line in code:
                    line = line.strip()
                    if line.startswith("fn("):
                        func_name = line[3:-1]
                        if func_name in functions:
                            for func_line in functions[func_name]:
                                exec(func_line.strip(), globals())
                        else:
                            print(f"Error: Function '{func_name}' not found.")
                    else:
                        print(f"Error: Invalid code '{line}'.")
            button.config(command=on_click)
            print(f"Click event bound to button '{name}'.")
            return
    print(f"Error: Button '{name}' not found.")
