
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if not nums:
        return 0
    if max(nums) < 0: 
        return max(nums)

   #Implementation of Kadane's Algorithm
   
    maxSum = 0
    currSum = 0 

    for i in range(len(nums)): 
        currSum = currSum + nums[i]
        if(currSum > maxSum): 
            maxSum = currSum
        if(currSum < 0):
            currSum = 0
    return maxSum
