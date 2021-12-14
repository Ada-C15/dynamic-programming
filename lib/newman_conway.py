

# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num == 0:
        raise ValueError
    
    return " ".join([str(x) for x in conway_recursive(num)])

def conway_recursive(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1, 1]

    ret_list = conway_recursive(num - 1)

    ret_list.append(ret_list[ret_list[num - 2] -1] + ret_list[num - ret_list[(num - 2)] -1])

    print(ret_list)
    return ret_list
