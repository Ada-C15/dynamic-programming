

def newman_conway(num):
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    '''
    if num < 1:
        raise ValueError
    elif num == 1:
        return "1"
    
    sequence = [0,1,1]

    for i in range(3, num+1):
        sequence.append(sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])
    return (" ".join(map(str, sequence[1:])))