
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    max_sum = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum = max((nums[i] + current_sum), nums[i])
        max_sum = max(current_sum, max_sum)
    if max_sum <=0:
        return max(nums)

    return max_sum


