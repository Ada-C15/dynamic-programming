
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)?
        Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    _max = 0 
    end = nums[0]

    for num in nums:
        _max = max(num, _max + num)
        end = max(end, _max)
    return end 
     




