# Fibannaci sequence in recursive function
def fib(n):
    # Make sure number is valid
    if n < 0:
        return ("Invalid Integer")
    # Base Case
    elif n == 0 or n == 1:
        return n
    # Recursive case
    else:
        return fib(n-1) + fib(n-2)

# Driver code
print(fib(5))

# Input 5
# Output 0 + 1 + 1 + 2 + 3 + 5 = 5