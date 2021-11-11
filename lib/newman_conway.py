

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num == 0:
        raise ValueError
    if num == 1:
        return '1'

    nc_sequence = [0, 1, 1]

    for i in range(3, num+1):
        nc = nc_sequence[nc_sequence[i-1]] + nc_sequence[i - nc_sequence[i-1]]
        nc_sequence.append(nc)

    return ' '.join([str(s) for s in nc_sequence[1:]])
