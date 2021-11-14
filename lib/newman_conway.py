#Newman Conway Sequence is the sequence which follows a 
#given recursive relation (p(n) = p(p(n-1)) + p(n-p(n-1))) 
#to generate a series of numbers. 

# Time complexity: ? Should be O(n) becuase processing time will depend on the size of n
# Space Complexity: Space complexity depends on how many memo's are taken? So O(n) maybe?

def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    
    #base case?
    if (num <= 0):
        #raise a value error?
        raise ValueError

    #create memoization array based on the input num
    memo = [0] * (num+1)
    print(f"memo initial: {memo}")

    #set inital values
    memo[0] = 0
    memo[1] = 1
    # memo[2] = 1
    print(f"memo: {memo}")

    # #im not sure how to deal with the cases of 1 and 2
    if num == 1:
        return '1'
    
    # #base case
    if (num == 2) :
        memo[2] = 1
        return '1 1'

    for i in range(3, num + 1):
        print(f"num: {num}")
        #(p(n) = p(p(n-1)) + p(n-p(n-1))) 
        memo[i] = memo[memo[num-1]] + memo[num - memo[num - 1]]
        print(f"new num: {num}")
        print(f"memo after loop: {memo}")
    
    return memo

    
    # i = 3
    # while (i <= num):
    # #collect nc sequence numbers
    #     memo[i] = memo[memo[i-1]] + memo[i - memo[i -1]]
    #     i += 1
    
    #return memo

    
