
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    if sum(nums) < 0:
        return max(nums)

    current_max = 0 
    total_max = 0 
    i = 0 

    while i < len(nums):
        current_max = current_max + nums[i] 
        if current_max > total_max:
            total_max = current_max
        i += 1
    return total_max

