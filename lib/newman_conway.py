

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError
    elif num == 1: 
        return "1"

    seq = [None, 1, 1]

    for i in range(3, num+1):
        seq.append(seq[seq[i-1]]+seq[i - seq[i-1]])
    return (" ".join(map(str, seq[1:])))

