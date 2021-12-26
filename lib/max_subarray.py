
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if nums == None or len(nums) == 0:
        return 0

    partial_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        if partial_sum + nums[i] < nums[i]:
            partial_sum = nums[i]
        else:
            partial_sum += nums[i]
            
        max_sum = max(max_sum, partial_sum)
        
    return max_sum
