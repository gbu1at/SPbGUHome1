import argparse
import typing as tp


def get_chars(text: str):
    return text.__len__()


def get_lines(text: str):
    return text.split('\n').__len__() - 1


def get_longest_line(text: str):
    return max(map(len, text.split('\n')))


def get_words(text: str):
    return len(text.split())


def convert_flags(flag: str) -> list:
    result = []
    for line in flag.split():
        result.extend([f'-{line[i]}' for i in range(1, line.__len__())])
    return result


def count_util(text: str, flags: tp.Optional[str] = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """

    if not flags:
        flags = "-mlLw"

    flags = convert_flags(flags)

    parser = argparse.ArgumentParser()

    parser.add_argument("-m", action="store_true")
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-L", action="store_true")
    parser.add_argument("-w", action="store_true")

    args = parser.parse_args(flags)

    print(args)

    result = dict()

    if args.m:
        result["chars"] = get_chars(text)

    if args.l:
        result["lines"] = get_lines(text)

    if args.L:
        result["longest_line"] = get_longest_line(text)

    if args.w:
        result["words"] = get_words(text)

    return result

