
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
    
    max_so_far = nums[0]
    max_ending = 0

    for i in range(len(nums)):

        max_ending = max_ending + nums[i]

        if max_so_far <= max_ending:
            max_so_far = max_ending

        if max_ending < 0:
            max_ending = 0

        # Moved before lines 23-24 because arr with all negative values
        # was resetting max_ending to 0 prematurely
        
        # if max_so_far <= max_ending:
        #     max_so_far = max_ending
    
    return max_so_far
