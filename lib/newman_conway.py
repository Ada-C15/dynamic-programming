

# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError("num cannot be zero")

    if num == 1:
        return "1"

    arr = [0, 1, 1] 

    for i in range(3, num+1): 
        arr.append(arr[arr[i-1]] + arr[i - arr[i-1]]) 

    string = ' '.join([str(item) for item in arr[1:]])

    return string 