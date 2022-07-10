def build_query(cmd, val, file):
    if cmd == 'filter':
        res = filter(lambda x: val in x, file)
    if cmd == 'map':
        val = int(val)
        res = map(lambda v, arg=val: v.split(' ')[arg], file)
        # val = int(val)
        # res = [x.split()[val] for x in file]
    if cmd == 'unique':
        res = set(file)
    if cmd == "sort":
        reverse = val == 'desc'
        res = sorted(file, reverse=reverse)
    if cmd == 'limit':
        val = int(val)
        res = list(file)[:val]
    return res
