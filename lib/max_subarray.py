
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    if max(nums) < 0:
        return max(nums)
    
    max_seen = 0
    max_ending_here = 0

    for num in nums:
        max_ending_here += num

        if max_ending_here < 0:
            max_ending_here = 0
                
        if max_seen < max_ending_here:
            max_seen = max_ending_here

    return max_seen
