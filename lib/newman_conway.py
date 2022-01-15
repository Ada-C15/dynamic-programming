

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    # <-------- NEWMAN CONWAY CONCEPT --------> 
    # P(1) = 1
    # P(2) = 1
    # for all n > 2
    # P(n) = P(P(n - 1)) + P(n - P(n - 1))

    # base case -> if num is either 0 or 1
    if num == 0:
        raise ValueError
    if num == 1:
        return '1'

    # P(1) = 1; P(2) = 1, P(3) = 2
    sequence = [0, 1, 1]

    # initialize string with starting values
    # remamnining values will be appended to string 
    newman_conway_str = "1 1 "

    # need to start range at index 3
    for i in range(3, num + 1):
        # calculating next value to append 
        sequence.append(sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])

        # must convert to string 
        newman_conway_str += f"{sequence[i]} "

    return newman_conway_str[:-1]
