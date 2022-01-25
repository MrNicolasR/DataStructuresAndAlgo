# Function 
def recRange(n):
    # Make sure number is valid
    if n < 0:
        return ("Enter a valid number")
    # Base Case
    elif n == 0:
        return 0
    # Recursive Case
    else:
        return n + recRange(n-1)
    
# Driver code
print(recRange(6))

# Input 10
# Output 0 + 1 + 2 + 3 + 4 + 5 + 6