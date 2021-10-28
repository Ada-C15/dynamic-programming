
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    # length of the list should equal num
    # 1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, ...
    # P(1) = 1
    # P(2) = 1
    # for all n > 2
    # P(n) = P(P(n - 1)) + P(n - P(n - 1))

    # raises exception if value is 0
    if num == 0:
        raise ValueError()

    # memo for calculations
    sequence = [0, 1, 1]

    # is the base case if num == 1 or num == 2?
    if num == 1:
        return str(sequence[1])
    if num == 2:
        string = ' '.join([str(item) for item in sequence[1:]])
        return string

    for i in range(3, num + 1):
        j = sequence[sequence[i-1]] + sequence[i-sequence[i-1]]
        sequence.append(j)

    string = ' '.join([str(item) for item in sequence[1:]])
    return string

print(newman_conway(2))
print(newman_conway(1))
# print(newman_conway(0))
