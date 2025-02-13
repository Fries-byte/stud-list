'''
*    interpret
'''

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
