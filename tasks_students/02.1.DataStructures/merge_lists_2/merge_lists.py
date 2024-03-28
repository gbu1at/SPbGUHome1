import heapq
import typing as tp


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """

    q = []

    for i in range(seq.__len__()):
        if seq[i].__len__() > 0:
            heapq.heappush(q, [seq[i][0], i, 0])

    res = []

    while q.__len__() > 0:
        val, idx_list, idx_val = heapq.heappop(q)
        if seq[idx_list].__len__() > idx_val + 1:
            heapq.heappush(q, [seq[idx_list][idx_val + 1], idx_list, idx_val + 1])
        res.append(val)

    return res

print(merge([[1, 2], [3, 4], [-1, 0]]))