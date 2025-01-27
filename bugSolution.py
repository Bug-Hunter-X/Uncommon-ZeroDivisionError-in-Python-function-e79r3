def function_with_uncommon_error(a, b):
    if a == 0 or b == 0:
        return None # or raise an exception like ZeroDivisionError("Division by zero")
    else:
        return a / b