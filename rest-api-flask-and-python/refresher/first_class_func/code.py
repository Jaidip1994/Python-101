def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division cannot be 0")
    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


calculate(5, 0, operator=divide)
