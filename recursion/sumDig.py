# Function
from math import floor


def sumDig(n):
    # Make sure is valid
    if n < 0:
        return ("Enter a valid number")
    # Base Case
    elif n == 0 :
        return 0
    # Recursive Case
    else:
        return n % 10 + sumDig(n//10)

print(sumDig(12341))

# Input 12341
# Output 1 + 2 + 3 + 4 + 1 = 11