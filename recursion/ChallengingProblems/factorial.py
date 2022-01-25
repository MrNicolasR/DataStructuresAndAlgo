# Function
def factorial(n):
    # Make sure number is valid
    if n < 0:
        return ("Enter a valid number")
    # Base case
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

print(factorial(7))