# Function
def pwrNum(x, n):
    # Make sure number is valid
    if n < 0:
        return ("Enter a valid number")
    # Base case
    elif n == 0:
        return 1
    elif n == 1:
        return x
    # Recursive Case
    else:
        return x * pwrNum(x, n-1) 

# Driver Code
print(pwrNum(2, 4))