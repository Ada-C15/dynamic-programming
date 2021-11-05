def max_sub_array(nums, memo={}):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    memo_key = str(nums)
    if memo_key in memo:
        max_sub_array(nums[1:], memo)
        max_sub_array(nums[:-1], memo)
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    memo[memo_key] = sum(nums)

    max_sub_array(nums[1:], memo)
    max_sub_array(nums[:-1], memo)

    sums = memo.values()
    max_sum = max(sums)
    return max_sum


# input = [50, -50, 50]
# input = [50, 3, -50, 50, 3]
input = [-3, -4, -5, -6, -7]
print(max_sub_array(input))
