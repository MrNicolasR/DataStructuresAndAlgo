# Function 
def toBinary(n):
    # Make sure number is valid
    if n < 0:
        return ("Enter a valid number")
    # Base case
    elif n == 0:
        return 0
    # Recursive case
    else:
        return n%2 + 10*toBinary(int(n/2))

# Driver Code
print(toBinary(4))
    