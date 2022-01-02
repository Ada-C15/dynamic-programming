

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

    sequence = [0, 1, 1]
    for val in range(3, num+1):
        nc = sequence[sequence[val - 1]] + sequence[val - sequence[val - 1]]
        sequence.append(nc)

    return ' '.join([str(s) for s in sequence[1:]])
