

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    if num < 1:
        raise ValueError("Invalid number")
    if num == 1:
        return "1"
    arr = [ 0, 1, 1]
    for i in range(3,num+1):
        arr.append(arr[arr[i - 1]] + arr[i - arr[i - 1]])

    arr = [str(item) for item in arr ]
    return " ".join(arr[1:])
    
