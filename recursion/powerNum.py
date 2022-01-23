# Function
def pwrNum(n, x):
    # Make sure number is valid
    if n < 0:
        return ("Enter a valid number")
    # Base case
    elif n == 0:
        return 1
    elif n == 1:
        return n
    # Recursive Case
    else:
        return x * x^(n-1) 

# Driver Code
print(pwrNum(4, 2))