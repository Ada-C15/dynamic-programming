

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError("ValueError")
    if num == 1:
        return '1'
    s='1 1'
    arr =[0,1,1]
    
    for num in range(3,num+1):
        new_num = arr[arr[num-1]]+arr[num -arr[num-1]]
        # i=3 arr[arr[2]]+arr[3-arr[2]]=arr[1]+arr[2]=2
        arr.append(new_num)
        s += " "+str(new_num)+''
    return s




    


    




