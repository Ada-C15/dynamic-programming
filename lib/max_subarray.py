
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
    
    temp_max = 0
    true_max = nums[0]

    for i in range(len(nums)):
        temp_max = max(nums[i], temp_max + nums[i])
        true_max = max(true_max, temp_max)

    return true_max
