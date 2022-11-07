def find_it(seq):
    for item in seq:
        if seq.count(item) %2:
            return item