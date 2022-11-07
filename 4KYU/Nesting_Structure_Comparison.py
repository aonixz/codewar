def same_structure_as(original,other):
    if type(original) != list or type(other) != list or len(original) != len(other) or type(original) != type(other):
        return False
    for x, y in zip(original, other):
        if type(x) != type(y) and x not in other:
            return False
        if type(x) == list and type(y) == list:
            return same_structure_as(x,y)
    return True