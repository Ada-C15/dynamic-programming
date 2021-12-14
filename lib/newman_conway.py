
# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """

    if num == 0:
        raise ValueError
    if num == 1:
        return '1'
    if num == 2:
        return '1 1'
    
    else:
        arr = [0, 1, 1]
        for count in range(3, num + 1):
            next_num = arr[arr[count-1]] + arr[count-arr[count-1]]
            arr.append(next_num)

        count_and_say = ' '.join([str(number) for number in arr[1:]])
        return count_and_say

        
        
        

