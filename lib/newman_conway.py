def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise(ValueError)
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    
    answer = [None, 1, 1]
    i = 3
    while i in range(3, (num + 1)):
        p = answer[answer[i - 1]] + answer[i - answer[i - 1]]
        answer.append(p)
        i += 1
    almost = answer[1:]
    final_answer = " ".join(str(n) for n in almost)
    return final_answer