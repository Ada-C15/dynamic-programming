

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError
    if num == 1:
        return '1'

    sequence = [0, 1, 1] 
    for i in range(3,num+1):
        sequence.append( sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])
    return ' '.join([str(s) for s in sequence[1:]])

    # updating our list of memos memoization 
    # taking a memo each time until you get up to num.

    # we start the sequence with [0, 1, 1]
    # the newman conway sequence doesnt start at 0 but indexing does
    # we needed something to put at the head of the list 
    # this is why we slice the return string to exclude the index[0] element
