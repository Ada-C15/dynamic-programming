
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
    
    cur = 0
    res = nums[0]

    for i in range(len(nums)):
        cur = max(nums[i], cur + nums[i])
        res = max(res, cur)

    return res
