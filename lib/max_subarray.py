
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    maxSum = 0
    currentSum = 0

    for i in range(len(nums)):
        currentSum = max((nums[i] + currentSum), nums[i])
        maxSum = max(currentSum, maxSum)
    
    if maxSum <=0:
        return max(nums)
    
    return maxSum