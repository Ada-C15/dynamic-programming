
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(N*M) 
        Space Complexity: O(1)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    max = nums[0]
   
    for index in range(len(nums)): # O(n) N
        subarray_sum = nums[index] # O(1)
        for pointer in range(1,(len(nums))): # O(M) even though it is decreasing by 1 each iteration 
            if subarray_sum > max: # O(1)
                max = subarray_sum # O(1)
            subarray_sum = subarray_sum + nums[pointer]# O(1)
            
    return max
                
                
            







