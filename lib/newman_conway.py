

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num ==0:
        raise ValueError
    
    if num == 1:
        return '1'
    
    p = [0,1,1]
  
    for i in range(3, num+1):
        sum = p[p[i - 1]] + p[i - p[i - 1]]
        p.append(sum)
    return ' '.join(str(elem) for elem in p[1:])
