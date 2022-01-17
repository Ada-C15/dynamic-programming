def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError

    if num == 1:
        return '1'

    if num == 2:
        return '1 1'

    sequence = [0, 1, 1]
    for i in range(3, num + 1):
        next_num = sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]]
        sequence.append(next_num)
    
    string_sequence = [str(number) for number in sequence[1:]]
    string_sequence = ' '.join(string_sequence)
    return  string_sequence
