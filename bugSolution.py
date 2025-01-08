def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return 0  # Or raise a more descriptive exception
    elif a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a