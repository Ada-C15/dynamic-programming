from math import inf 

def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not nums or len(nums) == 0:
        return 0

    sum_so_far = 0  # from wherever we starting to where we are (array)
    max_sum_so_far = float('-inf')  # negative infinity!

    for num in nums:
        sum_so_far += num  # add it to the sum so far
        if sum_so_far > max_sum_so_far:  # check if num should be added
            max_sum_so_far = sum_so_far  # if so, update max, sum keeps on
            
        elif sum_so_far < 0:  # if it brings it below the max
            sum_so_far = 0  # start algorithm over
            
    return max_sum_so_far


