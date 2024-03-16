import typing as tp


def reformat_git_log_line(line: str) -> str:

    data = line.split('\t')
    log = data[0][:7]
    mes = data[-1]
    res = log + "." * (81 - log.__len__() - mes.__len__()) + mes

    return res

def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """

    for line in inp:
        out.write(reformat_git_log_line(line))
