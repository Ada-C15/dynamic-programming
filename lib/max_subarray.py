
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
    
    current_max = nums[0]
    max_subarray = nums[0]

    for i in range(1, len(nums)):
        current_max = max(current_max + nums[i], nums[i])
        max_subarray= max(max_subarray, current_max)

    return max_subarray
    

