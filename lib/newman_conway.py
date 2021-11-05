# Please note that I referenced the GeeksforGeeks solution in order to solve this problem
# I was having trouble figuring out how to use a loop to append to a list given
# the recursive nature of the problem

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newmanum Conway numbers for the givenum value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError

    if num == 1:
        return '1'

    newman_conway_seq = [0, 1, 1]
    newman_conway_seq_str = ""

    # start off by adding the two 1's to the return string
    newman_conway_seq_str += f"{newman_conway_seq[1]} "
    newman_conway_seq_str += f"{newman_conway_seq[2]} "

    # start at index 3 through num + 1
    for i in range(3, num+1):

        # add new value to next index based on newman_conway equation
        newman_conway_seq.append(newman_conway_seq[newman_conway_seq[i - 1]] + newman_conway_seq[i - newman_conway_seq[i - 1]])

        # add new value to next "index" in string
        newman_conway_seq_str += f"{newman_conway_seq[i]} "
    
    return newman_conway_seq_str[:-1]


    # Returning value from Newman-Conway sequence:

    # if num == 1 or num == 2:
    #   return 1
      
    # return P(P(num - 1)) + P(num - P(num - 1))

    # if num = 3

    # P(P(2)) + P(3 - P(2))
    # left-hand side:
    # num is now 2, and when passed through P
    # num == 2 so return 1

    # right-hand side:
    # P(3 - P(2))
    # P(2 - 1) is P(2) which returns 1
    # Therefore P(3 - 1)
    # or P(2) returns 1

    # 1 + 1 = 2
