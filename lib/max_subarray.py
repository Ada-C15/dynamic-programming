
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
    
    # default both variables to the first index b/c the first index is the max value and max ending thus far
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):

        max_ending_here = max(max_ending_here + nums[i], nums[i])

        # continue updating value of variable as we itr
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
