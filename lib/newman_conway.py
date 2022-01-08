

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a string of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num == 0:
        raise ValueError
    
    if num == 1:
        return "1"

    seq = [0, 1, 1]

    for i in range(3, num + 1):
        next_num = seq[seq[i-1]] + seq[i - seq[i-1]]
        seq.append(next_num)
    
    return ' '.join([str(n) for n in seq[1:num+1]])

print(newman_conway(9))
