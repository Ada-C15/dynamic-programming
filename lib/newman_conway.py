
def newman_conway(num, memo=None):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError

    if num == 1:
        return '1'

    if memo is None:
        memo = [0, 1, 1]

    while num >= len(memo):
        for i in range(3, num +1):
            memo.append(memo[memo[i -1]] + memo[i - memo[i - 1]])
    return ' '.join([str(s) for s in memo[1:]])


    
