# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

from collections import Counter

def scramble(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    has_portion = True

    for c in c2:
        if c not in c1 or c1[c] < c2[c]:
            has_portion = False
            break

    return has_portion