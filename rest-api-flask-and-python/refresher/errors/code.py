def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero")
    return dividend/divisor


grade = []
print("Welcome to Average grade program")
try:
    average = divide(sum(grade), len(grade))
    print(f"Average grade is {average}")
except ZeroDivisionError as e:
    print(e)
else:
    print("There are no grades in the list")
finally:
    print("Thank you!")
