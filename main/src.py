'''
*   ptd::main
*   adding input and print
'''

def pln(text, *args):  # Define print
    text = text.replace("*n", "\n")
    text = text.replace("*t", "\t")
    for var_name in variables:
        placeholder = "{" + var_name + "}"
        if placeholder in text:
            text = text.replace(placeholder, str(variables[var_name]))
    for i, arg in enumerate(args):
        placeholder = "{" + str(i) + "}"
        if placeholder in text:
            text = text.replace(placeholder, str(arg))
    print(text)

def let(var_name, value):
    if var_name.startswith("{") and var_name.endswith("}"):
        var_name = var_name[1:-1]
        if var_name in variables:
            var_name = variables[var_name]
    if value.startswith("{") and value.endswith("}"):
        value = value[1:-1]
        if value in variables:
            value = variables[value]

def iln(prompt):  # Define input line
    return input(prompt)
