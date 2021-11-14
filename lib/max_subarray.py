
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """

    #https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    #https://www.youtube.com/watch?v=ohHWQf1HDfU

    max_sum = 0
    current_max_sum = 0

    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    #logic:
    #set the new calc to previous until you determine if it is <> then previous

    #loop through nums 
    for i in range(len(nums)-1):
        print(f"current_max_sum: {current_max_sum}")
        current_max_sum = current_max_sum + nums[i]
        print(f"current_max_sum: {current_max_sum}")
    
    if max_sum < current_max_sum:
        max_sum = current_max_sum
        print(f"max_sum: {max_sum}")
    
    return max_sum


    
