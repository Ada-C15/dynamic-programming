# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.

        P(1) = 1
        P(2) = 1
        for all n > 2
        P(n) = P(P(n - 1)) + P(n - P(n - 1))

        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    sequence = [None, 1, 1]

    if num < 1:
        raise ValueError

    index = 3
    while index <= num:
        sequence.append(sequence[sequence[index - 1]] +
                        sequence[index - sequence[index - 1]])
        index += 1

    return " ".join([str(element) for element in sequence[1:num + 1]])
