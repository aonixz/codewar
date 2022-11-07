def longest_consec(strarr, k):
    if (len(strarr) == 0 or k > len(strarr) or k<0)  :
        return ""
    lst = ["".join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x :len(x))