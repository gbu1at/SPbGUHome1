def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """

    # tree
    value_type = [bool, int, float, complex]
    collection_type = [range, tuple, list, str]

    if type1 in value_type and type2 in value_type:
        return value_type[max(value_type.index(type1), value_type.index(type2))]

    elif type1 in collection_type and type2 in collection_type:
        if (type1 == type2) and (type1 == range): return tuple
        return collection_type[max(collection_type.index(type1), collection_type.index(type2))]

    return str
