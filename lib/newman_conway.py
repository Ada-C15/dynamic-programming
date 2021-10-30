
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    # if number is zero, throw error
    if num == 0:
        raise ValueError("can't be zero")
    # if number is 1, just return '1' or first num in sequence
    if num == 1:
        return "1"
    # Declare array to store sequence 
    num_array = [0, 1, 1] 

    for i in range(3,num+1): 
        num_array.append( num_array[num_array[i - 1]] + num_array[i - num_array[i - 1]])

    # turning array back into a string of numbers
    string = ' '.join([str(item) for item in num_array[1:]])
    return string
