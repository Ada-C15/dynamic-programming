
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: o(n)
        Space Complexity: 0(1)
    """

    if not nums:
        return 0

    max_return = nums[0]

    last_seen = nums[0]

    for i in range(1, len(nums)):

        last_seen = max(nums[i], last_seen + nums[i])
        max_return = max(last_seen, max_return)
        # last_seen = last_seen + nums[i]
        # if last_seen < 0:
        #     last_seen = 0
        # if last_seen > max_return:
        #     max_return = last_seen

    return max_return
