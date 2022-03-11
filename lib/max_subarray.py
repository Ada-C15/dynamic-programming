import sys

#To find the max sum of sub_array which includes values from left, mid and right of the nums array
def max_mid_array(nums, left, mid, right):
        
    # To find the max sum of the left, iterate backwards
    #from the mid num
    sum = 0
    left_sum = -sys.maxsize
    
    for i in range(mid, left-1, -1):
        sum = sum + nums[i]
        
        if (sum > left_sum):
            left_sum = sum

    #To find the max sum of right subarray iterate up(increasing index values)from the
    #num to the right of mid num(mid + 1).
    sum = 0
    right_sum = -sys.maxsize
    
    for i in range(mid + 1, right + 1):
        sum = sum + nums[i]
        
        if (sum > right_sum):
            right_sum = sum
        
    return (left_sum + right_sum)

#To find the max subarray    
def max_sub_array(nums, left=0, right=None):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        
        Time Complexity: Time complexity is O(nLogn) time because of the implementation of a Divide and Conquer approach, in which the max subarray of 
        the given array is found through comparing the left and right value of a recursively calculated mid-point. This method also recursively calls the 
        helper method; max_mid_array() which considers max subarrays that range from left to right across the mid-point, with an O(nLogn) time complexity. 
        
        Space Complexity: Space complexity should be O(nLogn) as well because, according to my research, space complexity is relative to the size of the 
        call stack, which decreases by 2 values with each recursive call.  
    """
    n = len(nums)
    
    if n == 0:
        return 0
    
    if right == None:
        right = n-1
    
    #base case == only one element
    if(left == right):
        return nums[left]

    mid = (left + right) // 2
    
    maximum_sum_left_subarray = max_sub_array(nums, left, mid)
    maximum_sum_right_subarray = max_sub_array(nums, left+1, right)
    maximum_sum_crossing_subarray = max_mid_array(nums, left, mid, right);

    return max(maximum_sum_left_subarray, maximum_sum_right_subarray, maximum_sum_crossing_subarray)
