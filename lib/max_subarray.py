
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
    max_sub = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 1:
            current_sum = 0
        current_sum += n
        max_sub = max(max_sub, current_sum)

    return max_sub
