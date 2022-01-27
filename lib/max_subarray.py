
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    if nums == None or len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]
    
    max_sum = nums[0] + nums[1]
    max_sum_here =  0

    for i in range(len(nums)):
        max_sum_here = max_sum_here + nums[i]
        if max_sum < max_sum_here:
            max_sum = max_sum_here
        if max_sum_here < 0:
            max_sum_here = 0

    return max_sum