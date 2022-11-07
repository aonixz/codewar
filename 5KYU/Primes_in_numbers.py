def getAllPrimeFactors(n):
    if (not isinstance(n, int)) or n <= 1:
        if n == 1:
            return [1]
        else:
            return []
    else:
        factors = []
        prime = 2
        while prime*prime <= n:
            while (n % prime) == 0:
                factors.append(prime)
                n //= prime
            prime += 1
        if n > 1:
            factors.append(n)
        return factors



def prime_factors(n):
    result = ""
    factors = getAllPrimeFactors(n)
    for i in sorted(set(factors)):
        count = factors.count(i)
        if count == 1:
            result += "({})".format(i)
        else:
            result += "({}**{})".format(i, count)
    return result