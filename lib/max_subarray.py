
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

## Dynamic Solution - Kadane's Algorithm
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    nums_size = len(nums)
    max_so_far = nums[0]
    curr_sum = 0

    for i in range(0, nums_size):
        curr_sum = curr_sum + nums[i]
        if curr_sum < 0:
            curr_sum = 0        
        elif (max_so_far < curr_sum):
            max_so_far = curr_sum
    for i in nums:
        if max_so_far < i:
            max_so_far = nums[i]

    return max_so_far

## iterative solution
## import math
    # if nums == None:
    #     return 0
    # if len(nums) == 0:
    #     return 0

    # window_size = len(nums)
    # max_sum = -math.inf

    # while window_size:
    #     window_sum = sum([nums[i] for i in range(window_size)])
    #     if max_sum < window_sum:
    #         max_sum = window_sum
    #     if max_sum < nums[-1]:
    #         max_sum = nums[-1]
    #     window_size -= 1
    # return max_sum
