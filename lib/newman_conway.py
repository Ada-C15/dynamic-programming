
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    # edge case
    if not num or num < 0:
        raise ValueError('num must be greater than 0')

    # Initialize Newman Conway sequence array
    newcons = [None] * (num+1)

    # base case
    if num == 1:
        return '1'

    newcons[1] = 1
    newcons[2] = 1

    i = 3  # index!!!!!!
    if num > 2:
        # i = 3  # @ index 3 (num 3)
        while i <= num:
            # P(n) = P(P(n - 1)) + P(n - P(n - 1))
            newcons[i] = newcons[newcons[i - 1]] + newcons[i - newcons[i - 1]]
            i += 1

    return (' '.join(str(a) for a in filter(None, newcons)))
