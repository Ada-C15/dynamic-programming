
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) because the number of calculations performed depends on the size of num.
        
        Space Complexity: Space complexity is also O(n) becuase newman_conway_nums array to store sequence values, 
        nm_sequence_without_leading_zero to store result with leading 0 removed and result a array to which the properly 
        formatted result is saved are created and the amount of space that they occupy will depend on the size of the given num. 
    """
    if num == 0:
        raise ValueError
    
    if num == 1:
        return '1'
    
    if num == 2:
        return '1 1'
    
    #array to store sequence values and provide starting values
    newman_conway_nums = [0, 1, 1]
    
    for i in range(3, num + 1):
        newman_conway_nums.append(newman_conway_nums[newman_conway_nums[i-1]] + newman_conway_nums[i-newman_conway_nums[i-1]])
    
    nm_sequence_without_leading_zero = [str(num) for num in newman_conway_nums if num != 0]
    result = " ".join(nm_sequence_without_leading_zero)
    
    return result

