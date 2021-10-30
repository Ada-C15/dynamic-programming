
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: o(n)
        Space Complexity: O(n)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0


    max_list = [0 for num in range(len(nums))]
    max_list[0] = nums[0]

    for num in range(1, len(nums)):
        max_list[num] = max(max_list[num-1]+nums[num], nums[num])
    return max(max_list)
    