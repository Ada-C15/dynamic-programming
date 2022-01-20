

# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num <= 0:
        raise ValueError("num cannot be less than 1")
    memo = [0] * (num+1)
    memo[0] = 0
    memo[1] = 1
    if num > 1:
        memo[2] = 1

    x = 3
    while x <= num:
        memo[x] = memo[memo[x - 1]] + memo[x - memo[x - 1]]
        x += 1

    memo.pop(0)
    memo = [str(int) for int in memo]
    return " ".join(memo)
