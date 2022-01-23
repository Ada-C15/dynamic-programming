
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
    
    if max(nums) < 0:
        return max(nums)

    left_pointer = 0
    right_pointer = 0

    for num in nums:
        right_pointer += num

        if right_pointer < 0:
            right_pointer = 0

        if left_pointer < right_pointer:
            left_pointer = right_pointer
    return left_pointer
