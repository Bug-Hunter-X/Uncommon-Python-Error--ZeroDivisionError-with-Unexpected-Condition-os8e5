def function_with_uncommon_error(a, b):
    if a == 0:
        return b  #This line will cause ZeroDivisionError if the function is called with a=0 and b=0
    return b / a