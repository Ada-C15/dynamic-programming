
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    best_sum = 0
    current_sum = 0

    for num in nums:
        current_sum = max(0, current_sum + num)
        best_sum = max(best_sum, current_sum)
    if best_sum <= 0:
        return max(nums)
    return best_sum
