# Function
def revString(strng):
    # Check String Length
    if len(strng) <= 1:
        return strng
    # Recursive Case
    else:
        return strng[len(strng)-1] + revString(strng[0:len(strng)-1])


# Driver Code
print(revString("nico"))

# Input nico
# Output ocin
