import typing as tp


def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """

    if type(None) == type1:
        return type2
    if type(None) == type2:
        return type1

    value_type = [bool, int, float, complex]
    collection_type = [tuple, str, list]

    if type1 in value_type and type2 in value_type:
        return value_type[max(value_type.index(type1), value_type.index(type2))]

    elif type1 in collection_type and type2 in collection_type:
        if (type1 == type2) and (type1 == range): return tuple
        return collection_type[max(collection_type.index(type1), collection_type.index(type2))]

    return list


def isNone(val: type) -> bool:
    return val in ['', None, []]


def recast_to_all_type(val: type, all_type: type):
    if isNone(val):
        return all_type()
    if all_type == list:
        if type(val) in [str, int, float, bool]:
            return [val]
        return list(val)
    return all_type(val)


def getType(val: type) -> type:
    tp = type(val)
    if isNone(val): return type(None)
    return tp


def convert_to_common_type(data: list[tp.Any]) -> list[tp.Any]:
    """
    Takes list of multiple types' elements and convert each element to common type according to given rules
    :param data: list of multiple types' elements
    :return: list with elements converted to common type
    """

    all_type = get_common_type(getType(data[0]), type(None))
    for i in range(1, data.__len__()):
        if not isNone(data[i]):
            all_type = get_common_type(all_type, getType(data[i]))

    if type(None) == all_type:
        all_type = str

    res = [None] * data.__len__()
    for i in range(data.__len__()):
        res[i] = recast_to_all_type(data[i], all_type)

    return res
