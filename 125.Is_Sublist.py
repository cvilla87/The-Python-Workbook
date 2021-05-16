def is_sublist(smaller: list, larger: list) -> bool:
    print(smaller, larger, end=' -> ')

    num_items = len(smaller)
    cont = 0  # Number of matches

    for n in larger:
        if smaller[cont] == n:
            cont += 1
        elif cont > 0:
            cont = 0  # Reset matches counter
        if cont == num_items:  # We finish the function call as soon as we have full match
            print('YES sublist')
            return True
    print('NO sublist')
    return False


is_sublist([8], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([9], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([3, 4], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([9, 0, 3], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([0, 2, 3, 4, 1, 4], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([8, 9, 0, 2, 3, 4], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([2, 3, 4, 5, 6], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([8, 9, 0, 2, 3, 4, 5, 6], [8, 9, 0, 2, 3, 4, 5, 6])
is_sublist([2, 3, 4], [2, 3, 0, 7, 2, 3, 4, 5, 6])
