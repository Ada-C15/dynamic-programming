

# Time complexity: ? O(n^2)
# Space Complexity: ? O(1)

def newman_conway(n):
    return_string = "1 1"
    f = [0, 1, 1]

    if n == 0:
        raise ValueError("Value Error")
    if n == 1:
        return "1"
    for i in range(3, n + 1):
        r = f[f[i-1]]+f[i-f[i-1]]
        f.append(r)
        return_string += " " + str(r) + ""

    print(return_string)
    return return_string
