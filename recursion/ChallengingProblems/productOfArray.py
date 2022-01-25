# Function
def productArray(arr):
    # Make sure is valid
    if len(arr) == 0:
        return 1
    # Recursive case
    else:
        return arr[0] * productArray(arr[1::])

# Array
arr = [1,2,3,4,5]

# Driver Code
print(productArray(arr))

# Input arr = [1,2,3,4,5]
# Output = 1*2*3*4*5 = 120