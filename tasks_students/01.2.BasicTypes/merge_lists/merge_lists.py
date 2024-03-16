def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """

    lst_res = []

    it_a = 0
    it_b = 0

    while True:
        if it_a == lst_a.__len__():
            lst_res.extend(lst_b[it_b:])
            break
        if it_b == lst_b.__len__():
            lst_res.extend(lst_a[it_a:])
            break
        if lst_a[it_a] < lst_b[it_b]:
            lst_res.append(lst_a[it_a])
            it_a += 1

        elif lst_a[it_a] >= lst_b[it_b]:
            lst_res.append(lst_b[it_b])
            it_b += 1

    return lst_res


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """

    return sorted(lst_a + lst_b)
