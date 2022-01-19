
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
        Does this have to be contiguous? 
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
# # Arrange
    # input = [50, 3, -50, 50, 3]
    # output = 56
    # input1 = [-2, -1]
    # output = [-1]
    
    max_so_far = 0
    max_ending = 0

    for i in nums:
        max_ending += i

        if  max_ending > max_so_far:
            max_so_far = max_ending

        # when max sum is less than 0/negative num 
        if max_so_far <= 0:
            return max(nums)
    return max_so_far

# Run Time: 0(n)
# Space: O(1)
