
def max_sub_array(nums, max_sum=None, current_sum=0, current_index=0):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    if not max_sum:
        max_sum = nums[0]
    if current_index == len(nums):
        if current_sum < max_sum and nums[current_index-1] > max_sum:
            max_sum = nums[current_index-1]
        return max_sum

    current_sum += nums[current_index]

    if current_sum >= max_sum:
        return max_sub_array(nums, max_sum=current_sum, current_sum=current_sum, current_index=current_index+1)
        
    if current_sum <= max_sum:
        return max_sub_array(nums, max_sum, current_sum, current_index=current_index+1)
    



