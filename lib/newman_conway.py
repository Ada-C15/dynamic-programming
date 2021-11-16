# [Newman-Conway sequence] is the one which generates the following integer sequence.  1 1 2 2 3 4 4 4 5 6 7 7….. and follows below recursive formula.

# P(1) = 1
# P(2) = 1
# for all n > 2
# P(n) = P(P(n - 1)) + P(n - P(n - 1))

def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    # Base cases: num is 0 or 1
    if num == 0:
        raise ValueError
    if num == 1:
        return '1'

    # P(1) = 1; P(2) = 1, P(3) = 2
    nc_seq_nums = [0, 1, 1]

    # The returned list has to be a string:
    nc_seq_str = "1 1 "

    for i in range(3, num + 1):
        # calculating next Newman-Conway sequence value and appending
        nc_seq_nums.append(nc_seq_nums[nc_seq_nums[i - 1]] + nc_seq_nums[i - nc_seq_nums[i - 1]])

        # must convert to string 
        nc_seq_str += f"{nc_seq_nums[i]} "

    return nc_seq_str[:-1]