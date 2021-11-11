def max_sub_array(nums, memo={}):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: o(n)
        Space Complexity: o(n)
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
