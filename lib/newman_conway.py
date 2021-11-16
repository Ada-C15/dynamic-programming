

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: ?
    """
    if(num == 0):
        raise ValueError
        
    memo = []

    if (num == 1):
        memo = [0, 1]
    elif (num == 2):
        memo = [0, 1, 1]
    else:
        memo = [0, 1, 1]
        num_terms = len(memo) - 1 # ignore element at index 0
        for i in range(3, num + 1):
            memo.append( memo[memo[i-1]] + memo[i - memo[i-1]] )

    memo.pop(0) # remove element at index 0
    converted_list = [str(element) for element in memo]
    return " ".join(converted_list)