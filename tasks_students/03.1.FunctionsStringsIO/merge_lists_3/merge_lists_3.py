import typing as tp
import heapq


def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """

    q = []

    seq = [input_streams[i] for i in range(input_streams.__len__())]

    for i in range(seq.__len__()):
        if seq[i].__len__() > 0:
            heapq.heappush(q, [seq[i], i, 0])

    res = []

    while q.__len__() > 0:
        val, idx_list, idx_val = heapq.heappop(q)
        if seq[idx_list].__len__() > idx_val + 1:
            heapq.heappush(q, [val, idx_list, idx_val + 1])
        res.append(val)

    output_stream.write(bytes(res))