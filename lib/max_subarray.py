
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

    max_sub_array = 0
    sum = 0

    for num in nums:
        sum = max(0, sum + num)
        max_sub_array = max(max_sub_array, sum)
    if max_sub_array <= 0:
        return max(nums)
    return max_sub_array
