

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: o(n)
        Space Complexity: 0(n)
    """
    # count of num and the num itself 
    # input = 13
    # output = 1113 -> 3113 -> 132113-> 1113122113 -> 311311222113 -> 13211321322113 ->
    if num == 0:
        raise ValueError
    if num == 1:
        return "1"

    sequence = [0, 1, 1]
    for val in range(3, num+1):
        nc = sequence[sequence[val - 1]] + sequence[val - sequence[val - 1]]
        sequence.append(nc)

    return ' '.join([str(s) for s in sequence[1:]])

