

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    
    if num == 0:
        raise ValueError
    
    if num == 1:
        return '1'
    
    res = [0,1,1]

    for i in range(3, num+1):
        sum = res[res[i-1]] + res[i-res[i-1]]
        res.append(sum)

    return ' '.join(str(num) for num in res[1:])