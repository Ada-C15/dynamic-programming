
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: o.n
        Space Complexity: o.1
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    else:
        max = nums[0]
        max_array = 0
        sub_array_sum = 0

        for num in nums:
            max_array += num
            sub_array_sum += num
            if num > max:
                max = num
            if sub_array_sum > max_array:
                max_array = sub_array_sum
            elif max_array > max:
                max = max_array
        return max
        
        
            

