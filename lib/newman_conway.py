

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) single for loop to find nth element of sequence - linear
        Space Complexity: O(n) use list to store cache which is required to compute nth element - linear
    """
    if num == 0:
        raise ValueError("Number cannot be zero")
    elif num == 1:
        return "1"

    cache = [0,1,1]
    
    for i in range(3, num + 1): 
        cache.append(cache[cache[i-1]] + cache[i - cache[i-1]]) 
    string = ' '.join([str(item) for item in cache[1:]])
    
    return string 
