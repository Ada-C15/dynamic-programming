

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity:O(n)
    """
    # base case , storage is None
    if num == 0:
        raise ValueError("input cannot be zero")
    # base case , input is 1
    if num == 1:
        return "1"

    # base case list for input 2
    number_list = [0, 1, 1]
    # for index in range, append to list
    for i in range(3, num+1):
        number_list.append(
            number_list[number_list[i - 1]] + number_list[i - number_list[i - 1]])
    # list comprehension, joined by space
    final_string = ' '.join([str(item) for item in number_list[1:]])
    return final_string
