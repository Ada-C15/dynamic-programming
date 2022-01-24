

# Time complexity: O(1)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num == 0:
        raise ValueError

    if num == 1:
        return "1"

    if num == 2:
        return "1 1"

    initial_list = [0, 1, 1]
 
    for i in range(3, num + 1):
        new = initial_list[initial_list[i-1]]+initial_list[i-initial_list[i-1]]
        initial_list.append(new);

    return_string = [str(num) for num in initial_list[1:]]
    return_string = " ".join(return_string)
    return return_string
