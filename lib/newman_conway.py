

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num == 0:
        raise ValueError

    arr  = [0,1,1]
    for i in range(3,num + 1):
        r = arr[arr[i-1]]+arr[i-arr[i-1]] 
        arr.append(r)
    
    string_array = []
    for num in arr[1:]:
        string_array.append(str(num))
    string_array = ' '.join(string_array)
        
    return string_array

