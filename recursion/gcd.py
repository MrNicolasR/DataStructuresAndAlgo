# Function 
def gcd(a, b):
    # Make sure numbers are valid
    if a < 0 or b < 0:
        return ("Enter a valid number")
    # Base Case
    elif b == 0:
        return a
    # Reacursive case
    else:
        return gcd(b, a % b)

# Run function
print(gcd(48,36))