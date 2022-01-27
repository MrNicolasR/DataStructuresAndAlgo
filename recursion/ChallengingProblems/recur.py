# Is Odd Function
def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

# Recusive function
def someRecursive(arr, cb):
    # Make Sure array is valid
    if len(arr) == 0:
        return False
    # Recursive case
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True


# array
arr = [2, 4, 6]

# Driver code
print(someRecursive(arr, isOdd))

# Input arr
# Output False
