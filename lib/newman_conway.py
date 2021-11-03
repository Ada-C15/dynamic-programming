

# Time complexity: ?
# Space Complexity: ?

# newman
''' 1     1       2       2       3       4   
    P(1)   P(2)    P(3)    P(4)    P(5)    P(6)'''

# P(1) = 1
# P(2) = 1
# for all n > 2
'''P(n) = P(P(n - 1)) + P(n - P(n - 1))'''

# P[1] = P(P(1-1)) + P(1 - P(1-1))
# P[2] = P(P(2-1)) + P(2 - P(2-1))
# P[3] = P(P(3-1)) + P(3 - P(3-1))
'''P(3)     =       P(       P(2)     +         P(3 - P(2)    )   )'''
'''newcon   =   newcon( newcon(num-1) +    newcon(num -)           '''
'''                     newcon_2 + newcon                    '''
# P(3) =    (1) + P(3 - (1))
# P(3) =    (1) + P(2)
# P(3) =     1  + 1

#  memo P(1) and P(2)
#  call a recursive formula that uses the memo

# f(n) = f(n-1) + f(n-2)
# fib = fib(n-1) + fib(n-2)

# fib = [None] * (n+1)

# fib[0] = 1

# def newman_conway(num):
#     """ Returns a list of the Newman Conway numbers for the given value.
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     if not num or num < 0:
#         raise ValueError('num must be greater than 0')
#     # base case
#     if num == 1 or num == 2:
#         return 1

#     # memo

#     p = p(p(num-1) + p(n - p(num-1)))
#      
#     # memo
#     newcon_1 = 1
#     newcon_2 = 1

#     num > 2: 
#     pass


# def newman_conway(num):
#     """ Returns a list of the Newman Conway numbers for the given value.
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     # edge case
#     if not num or num < 0:
#         raise ValueError('num must be greater than 0')

#     newcons = [None] * (num-1)
#     print(newcons)
    
#     # base case
#     if num == 1:
#         # return str(1)
#         newcons[0] = 1
#     if num == 2:
#         newcons[1] = 1
#         # return '1 1'
        
#     # I DONT THINK I NEED THIS
#     # # memo num = 1
#     # newcons[0] = 1
#     # # memo num =
#     # newcons[1] = 1

#     n = 3  # @ index 2 # while 3 < num (num = 13)
#     while n <= num:
#         # nc_prev = n-1
#         nc_prev = newcons[num-1]
#         # nc_prev_prev = n - nc_prev
#         nc_prev_prev = n - nc_prev
#         newcons[num] = nc_prev + nc_prev_prev

#         # '''p[n] =   nc_prev    +       n - nc_prev      '''

#         # P[n] = P  (P(n - 1))  + P(    n - P(n - 1))

#         # P(3) = P  (P(3-1))    + P(    3 - P(3-1))

#         # P(3) = P  (P(2)       + P(    3 - P(2)))

#         # P(3) = P  (P(2)       + P(    3 - 1   ))) <--P(n - 2) = newcons_nc_prev = newcons(n - newcons_prev)
#         #             ^
#         #             1  <--P(2) =    newcons_prev
#         # p [3]   =   P       (nc_prev    + P(    n - nc_prev) )
#         # newcons =   P       (nc_prev    + nc_prev_prev       ) 
#         # newcons = newcons   (nc_prev    + nc_prev_prev      )                             
        
#         # newcons[n] = newcons[newcons[n - 1]] + newcons[n - newcons[n - 1]]
#         # newcons[n] = newcons[newcons[n - 1]] + newcons_prev


#         n += 1
    
#     # n for n in newcons print(n)]
#     return (''.join(str(n) for n in newcons))


def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    # edge case
    if not num or num < 0:
        raise ValueError('num must be greater than 0')

    newcons = [None] * (num+1)
    print(newcons)
    
    # base case
    if num == 1:
        newcons[1] = 1
        return (' '.join(str(a) for a in filter(None, newcons)))
    if num == 2:
        newcons[1] = 1
        newcons[2] = 1
        return (' '.join(str(a) for a in filter(None, newcons)))
        
    newcons[1] = 1
    newcons[2] = 1

    i = 3  # index!!!!!!
    if num > 2:   

        # i = 3  # @ index 3 (num 3) 
        while i <= num:
            '''P(n) = P(P(n - 1)) + P(n - P(n - 1))'''

            newcons[i] = newcons[newcons[i - 1]] + newcons[i - newcons[i - 1]]
            i += 1
    
    return (' '.join(str(a) for a in filter(None, newcons)))