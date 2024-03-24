def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """

    if path.__len__() == 0:
        return "."

    t = path.split('/')

    res = []

    is_root_folder = (path[0] == '/')

    for v in t:
        if v == '':
            continue
        if v == '.':
            continue
        elif v == '..':
            if res.__len__() == 0:
                if not is_root_folder:
                    res.append('..')
            elif res[-1] != '..':
                res.pop()
            elif res[-1] == '..':
                res.append('..')
            else:
                assert False
        else:
            res.append(v)
    if res.__len__() == 0:
        if not is_root_folder:
            return '.'
        return '/'
    ans = '/'.join(res)
    if is_root_folder:
        ans = '/' + ans
    return ans

# print(normalize_path('/////documents/root/.././../etc'))
