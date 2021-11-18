

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num, storage=None):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if storage is None:
        storage = [None, 1, 1]

    if num == 0:
        raise ValueError

    while num >= len(storage):
        storage.append(storage[storage[-1]] + storage[len(storage) - storage[-1]])

    str_storage = [str(num) for num in storage[1:num+1]]
    return " ".join(str_storage)
    