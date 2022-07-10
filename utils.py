def build_query(cmd, val, file):
    if cmd == 'filter':
        res = filter(lambda x: val in x, file)
        return res
    if cmd == 'map':
        val = int(val)
        res = [x.split()[val] for x in file]
        return res
    if cmd == 'unique':
        return list(set(file))
    if cmd == "sort":
        reverse = val == 'desc'
        res = sorted(file, reverse=reverse)
        return res
    if cmd == 'limit':
        val = int(val)
        res = list(file)[:val]
        return res

