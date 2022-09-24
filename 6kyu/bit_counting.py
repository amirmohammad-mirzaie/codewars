
# https://www.codewars.com/kata/526571aae218b8ee490006f4

def countBits(n):
    list = []
    l = helpCount(n, list)
    return sum(l)

def helpCount(n, list):
    if n > 1:
        helpCount(n//2, list)
    list.append(n%2)
    return list