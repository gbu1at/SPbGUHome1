import typing as tp


def filter_list_by_list(lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range]) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """

    lst_res = []

    it_a = 0
    it_b = 0

    while it_a < lst_a.__len__():
        if it_b == lst_b.__len__():
            lst_res.extend(lst_a[it_a:])
            break

        if lst_a[it_a] < lst_b[it_b]:
            lst_res.append(lst_a[it_a])
            it_a += 1
        elif lst_a[it_a] == lst_b[it_b]:
            it_a += 1
        else:
            it_b += 1

    return lst_res
