'''
*   ptd::main
*   Contains the core interpreter logic.
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

def fn(name=None, variable=None, code=None):
    if name and code:
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = {"code": lines, "variable": variable}
        if name == "main":
            for line in lines:
                if line.startswith("define("):
                    exec(line, globals())
                else:
                    slice(line)
    elif name in functions:
        func = functions[name]
        if func["variable"] is not None:
            for line in func["code"]:
                updated_line = line.replace(f"{{{func['variable']}}}", str(variable))
                slice(updated_line)
        else:
            for line in func["code"]:
                slice(line)
    else:
        print(f"Function '{name}' not found.")

def if_stmt(var, value, code_if, code_else=None):
    if var in variables:
        if variables[var] == value:
            try:
                for line in code_if:
                    if callable(line): 
                        line()
                    else:
                        exec(line.strip(), globals())
            except Exception as e:
                print(f"Error in if condition block: {e}")
        elif code_else:
            try:
                for line in code_else:
                    if callable(line):
                        line()
                    else:
                        exec(line.strip(), globals())
            except Exception as e:
                print(f"Error in else condition block: {e}")
    else:
        print(f"Error: Variable '{var}' not found.")

def loop(code, n):
    if n == 0:
        while True:
            execute_main(code)
    else:
        for _ in range(n):
            execute_main(code)

def catch(code, error_handler):
    try:
        exec(code, globals())
    except Exception as e:
        error_message = str(e)
        for line in error_handler:
            line = line.replace("{!error!}", "Error Found").replace("{!reason!}", error_message)
            exec(line, globals())

def execute_main(code):  
    line_num = 0
    for line in code.splitlines():
        line_num += 1
        stripped_line = line.strip()
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()
        if stripped_line == "":
            continue
        try:
            if stripped_line in custom_keys:  
                custom_keys[stripped_line]()
            else:
                parts = stripped_line.split(" ", 1)
                if parts[0] in custom_keys:
                    if len(parts) > 1:
                        custom_keys[parts[0]](parts[1])
                    else:
                        custom_keys[parts[0]]("")
                else:
                    exec(stripped_line, globals())
        except Exception as e:
            print(f"Error on line {line_num}: {e}")
            return line_num
    return None
