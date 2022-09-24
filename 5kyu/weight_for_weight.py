# https://www.codewars.com/kata/55c6126177c9441a570000cc


def sum_digits(num):
    summ = 0
    while num:
        summ += (num%10)
        num = num//10
    return summ


def order_weight(strng):
    # your code
    split = strng.split()
    split = sorted([(sum_digits(int(item)), item) for item in split])
    result = ' '.join(item[1] for item in split)

    return result
