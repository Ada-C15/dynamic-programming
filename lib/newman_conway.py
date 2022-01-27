

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError("Input must be an integer larger than 0")

    if num == 1:
        return "1"

    seq = [1, 1]
    i = 3

    while i <= num:
        n = seq[seq[i - 2] - 1] + seq[i - seq[i - 2] - 1]
        seq.append(n)
        i += 1

    printed_seq = ""
    for n in seq:
        printed_seq += str(n) + " "

    return printed_seq[0:-1]