
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
    
    max_so_far = nums[0]
    max_ending_here = 0

    for num in nums:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here != 0 and max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here == 0:
            max_so_far = max(max_so_far, num)

    return max_so_far
