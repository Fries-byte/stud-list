'''
 * ptd::utils
 * Contains utility functions.
'''

import webbrowser
from tkinter import messagebox

def wo(url):
    webbrowser.open(url)

def mb(type, title, message):
    method_name = "show" + type
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")
