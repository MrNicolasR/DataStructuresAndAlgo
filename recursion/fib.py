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
print("\nFn is: %d\n" % fib(6))