from math import inf 

def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    # if nums == None:
    if not nums or len(nums) == 0:
        return 0

    sum_so_far = 0  # from wherever we starting to where we are (array)
    # max_sum_so_far = 0      # nums[i]
    max_sum_so_far = float('-inf')  # negative infinity!
    for num in nums:
        sum_so_far += num
        # check if it's worth including the number
        if sum_so_far > max_sum_so_far:
            max_sum_so_far = sum_so_far
        # elif sum_so_far < 0:
        #     # sum_so_far = 0  # start algorithm over
        #     sum_so_far = sum_so_far + num
        elif sum_so_far < 0:
            max_sum_so_far = num
    return max_sum_so_far


# [10, -20, 30, 3, -50, 10]

# biggest number we added so far
# sum so far
