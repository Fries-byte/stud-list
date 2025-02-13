'''
 * ptd::sys
 * Will add system/outside functions.
'''

def py(execpython):
    exec(execpython)

def bash(executeos):
    output = os.popen(executeos).read()
    print(output)
