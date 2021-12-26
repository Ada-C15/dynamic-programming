

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Recursive formula:
        P(1) = 1
        P(2) = 1
        for all n > 2
        P(n) = P(P(n - 1)) + P(n - P(n - 1))

        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError

    if num == 1:
        return "1"

    seq = [0, 1, 1] 

    for i in range(3,num+1): 
        seq.append( seq[seq[i - 1]] + seq[i - seq[i - 1]]) 


    final_string = ' '.join([str(item) for item in seq[1:]])
    return final_string 
