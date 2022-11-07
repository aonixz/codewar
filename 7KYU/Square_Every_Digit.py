def square_digits(num):
    res = ""
    for item in str(num):
        res +=str(int(item)**2)
        tmp = int(res)
    return tmp