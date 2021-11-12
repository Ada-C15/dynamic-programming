# Input : 13
# Output : 1 1 2 2 3 4 4 4 5 6 7 7 8

# Time complexity: o(n)
# Space Complexity: o(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
        p(4) = p(p(3)) + P(4-(P(3)))
        p(4) = 1 + 1 = 2 
        p(3) = p(p(2)) + p(3-(P(2)))
        p(3) = 1 + 1 = 2 

        P(1) = 1
        P(2) = 1
        for all n > 2
        P(n) = P(P(n - 1)) + P(n - P(n - 1))

    """
    # we know that p(1) and p(2) always equal 1
    if num == 0:
        return None
    if num == 1:
        return 1

    # if we solve for every number from 3 - n, we will have the answer for the one before it, we can use that in the algorithm.
    sequence = [0, 1, 1]

    for i in range(3, num + 1):
        sequence.append(sequence[sequence[i - 1]] +
                        sequence[i - sequence[i - 1]])

    return (" ".join(map(str, sequence[1:])))
