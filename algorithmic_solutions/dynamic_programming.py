def fibonacci_dynamic_recursive(position):
    memoized_values = {}
    if position < 0:
        raise ValueError('position has to be 0 or positive.')
    if position == 0:
        return 0
    if position == 1 or position == 2:
        return 1
    else:
        memoized_position = memoized_values.get(position, None)
        if memoized_position:
            return memoized_position
        computed_value = fibonacci_dynamic_recursive(position-1) + fibonacci_dynamic_recursive(position-2)
        memoized_values[position] = computed_value
        return computed_value


def fibonacci_dynamic_norecursive(position):
    """
    These both solutions reduce complexity of the classic recursive solution from O(2^n) to only O(2n+1).
    With this approach we also avoid problem with recursion when recursion depth is too big.
    :param position:
    :return: Fibonacci number at the position
    """
    first_value, second_value = 1, 1
    if position < 0:
        raise ValueError('position has to be 0 or positive.')
    if position == 0:
        return 0
    if position == 1 or position == 2:
        return 1
    else:
        for n in range(3, position+1):
            swap = second_value
            second_value = first_value + second_value
            first_value = swap
        return second_value


def find_expensive_path_value(tree):
    """
    Dynamic programming example, solving problem of searching the most expensive path
    in the randomly big tree structure:

            4
          2   4
        5   7   12
        .
        .
        .

    Tree is represented by a list.
    Algorithm is going bottom-up, always replacing one level upper layer with the best temporally computed values.
    Solution and description from:
    https://hackernoon.com/dynamic-programming-python-80f944aa6e6c

    """
    total = 0
    temp_list = []
    print(tree)
    while len(tree) is not 1:
        if len(tree) == 2:
            print(max(tree[-1]))
            print(tree[0][0])
            total = max(tree[-1]) + tree[0][0]
        if tree[-2][-1] + tree[-1][-1] > tree[-2][-1] + tree[-1][-2]:
            tree[-2][-1] = tree[-2][-1] + tree[-1][-1]
        else:
            tree[-2][-1] = tree[-2][-1] + tree[-1][-2]
        temp_list.insert(0, tree[-2][-1])
        del tree[-1][-1]
        del tree[-2][-1]
        if len(tree[-2]) == 0:
            tree[-1] = temp_list
            del tree[-2]
        print(tree)
        print(temp_list)
    print(total)


position = fibonacci_dynamic_recursive(36)
print(position)