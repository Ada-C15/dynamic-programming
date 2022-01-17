

# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a string of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError
    
    if num == 1:
        return "1"

    if num == 2:
        return "1 1"
    
    nums = [0, 1, 1]

    for i in range (3, num + 1):
        nums.append( nums[nums[i-1]] + nums[i - nums[i-1]])
        
    return " ".join([str(item) for item in nums[1:num+1]])

