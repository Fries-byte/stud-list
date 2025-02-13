'''
 * ptd::math
 * Contains math-related functionality.
'''

def math(expression):
    try:
        for var_name, var_value in variables.items():
            placeholder = "{" + var_name + "}"
            if placeholder in expression:
                expression = expression.replace(placeholder, str(var_value))
        return eval(expression, {}, variables)
    except Exception as e:
        print(f"Error evaluating math expression: {e}")
        return None
