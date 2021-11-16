
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

    final_max = nums[0]
    current_max = 0

    for i in range(len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        final_max = max(final_max, current_max)

    return final_max
