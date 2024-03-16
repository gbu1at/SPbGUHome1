import typing as tp


def find_value(nums: tp.Union[list[int], range], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """

    if nums.__len__() == 0:
        return False

    l = 0
    r = nums.__len__()

    while l < r - 1:
        m = (l + r) // 2
        if nums[m] == value:
            return True
        elif nums[m] < value:
            l = m
        else:
            r = m

    return nums[l] == value
