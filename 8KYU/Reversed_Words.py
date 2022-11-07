def reverse_words(s):
    tmp = []
    for item in s.split(" "):
        tmp.append(item)
    return " ".join(tmp[len(tmp)::-1])