
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if not nums or len(nums) == 0:
        return 0

    global_max = float("-inf")
    current_max = float("-inf")

    for num in nums:
        current_max = max(num + current_max, num)
        global_max = max(current_max, global_max)

    return global_max
