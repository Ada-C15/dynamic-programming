
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_ = 0 
    end = nums[0]

    for num in nums:
        max_ = max(num, max_ + num)
        end = max(end, max_)
    return end 
     




