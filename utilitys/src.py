'''
 * ptd::utils
 * Contains utility functions.
'''

import webbrowser
from tkinter import messagebox
import urllib.request

def wo(url):
    webbrowser.open(url)

def mb(type, title, message):
    method_name = "show" + type
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def load(packport):
    try:
        # Fetch the raw content from the URL
        response = urllib.request.urlopen(packport)
        raw_content = response.read().decode()
        
        # Extract executable code (ignore comments and non-code lines)
        executable_code = []
        for line in raw_content.splitlines():
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("'''") and not stripped_line.startswith('#'):
                executable_code.append(stripped_line)
        
        # Execute the extracted code
        exec("\n".join(executable_code), globals())
    except Exception as e:
        print(f"Error loading package from {packport}: {e}")
