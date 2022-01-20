
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    now_max = 0
    max_ending_here = nums[0]

    for i in range(len(nums)):
        now_max = max(nums[i], now_max + nums[i])
        max_ending_here = max(max_ending_here, now_max)
    return max_ending_here

