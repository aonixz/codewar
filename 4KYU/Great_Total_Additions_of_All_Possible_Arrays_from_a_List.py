import itertools

def gta(limit, *args):
    gta_value = 0
    new = []
    for i in itertools.zip_longest(*[str(i) for i in args]):
        for n in i:
            if n != None and int(n) not in new:
                new.append(int(n))
    for contr in range(limit + 1):
        for numb in itertools.permutations(new[:limit], contr):
            gta_value += sum(numb)

    return gta_value