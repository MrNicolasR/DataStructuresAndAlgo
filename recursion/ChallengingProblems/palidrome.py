# Function
def palindrome(strng):
    # Base Case
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    # Recursive
    return palindrome(strng[1:-1])


# Driver Code
print(palindrome("bob"))

# Input bob
# Output True
