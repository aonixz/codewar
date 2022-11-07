def digitize(n):
    res = str(n)[::-1]
    lst = []
    for i in res:
        lst.append(int(i))
    return lst