
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    size = len(nums)
    if size == 0:
        return 0
    dp = [0 for _ in range(size)]
    for i,num in enumerate(nums):            
        dp[i] = max(dp[i-1] + num, num)
    return max(dp)


    # if nums == None:
    #     return 0

    # if len(nums) == 0:
    #     return 0

    # max_so_far =nums[0]
    # curr_max = nums[0]
    
    # for i in range(1,len(nums)):
    #     curr_max = max(nums[i], curr_max + nums[i])
    #     max_so_far = max(max_so_far,curr_max)
    # return max_so_far
