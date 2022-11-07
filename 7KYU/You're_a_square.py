from math import sqrt
def is_square(n):
    if n>=0:
        if round(sqrt(n)) **2 == n:
            return True
    return False