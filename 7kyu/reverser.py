
# https://www.codewars.com/kata/58069e4cf3c13ef3a6000168

def help_reverse(n, b):
    while n//10:
        r = n%10
        b = b*10 + r
        n = n//10
    b = b*10 + n
    return b

def reverse(n):
    b = 0
    reversedNumber = help_reverse(n, b)

    return reversedNumber