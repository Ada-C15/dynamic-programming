def newman_conway(num: int):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(nm)
        Space Complexity: O(nm)
    """
    if num <= 0:
        raise ValueError
    if num == 1:
        return "1"

    sequence = [None] * (num+1)
    sequence[0] = 0
    sequence[1] = 1
    sequence[2] = 1
    find_newman_conway(num, sequence)
    return " ".join(map(str, sequence[1::]))

def find_newman_conway(num: int, sequence: list) -> int:
    if num < len(sequence) and sequence[num]:
        return sequence[num]
    else:
        val = find_newman_conway(find_newman_conway(num - 1, sequence), sequence) + find_newman_conway(num - find_newman_conway(num - 1, sequence), sequence)
        sequence[num] = val
        return val