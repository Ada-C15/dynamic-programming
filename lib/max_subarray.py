
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
    if len(nums) == 1:
        return nums[0]

    max_so_far = nums[0]
    max_ending_here = 0

    for i in range(len(nums)):
        if max_ending_here < 0:
            max_ending_here = 0
        max_ending_here += nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far
