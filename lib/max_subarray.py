
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

    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
      #print(dp)
    return max(dp)
