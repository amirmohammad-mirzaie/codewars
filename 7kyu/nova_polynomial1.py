# https://www.codewars.com/kata/570ac43a1618ef634000087f

def poly_add(p1, p2):
    p1Len = len(p1)
    p2Len = len(p2)

    isBigger = False
    if p1Len > p2Len:
        isBigger = True
    result = []
    if p1Len > p2Len:
        for i in range(p1Len):
            if i < p2Len:
                result.append(p1[i] + p2[i])
            else:
                result.append(p1[i])
    elif p1Len == p2Len:
        for i in range(p1Len):
            result.append(p1[i] + p2[i])
    else:
        for i in range(p2Len):
            if i < p1Len:
                result.append(p1[i] + p2[i])
            else:
                result.append(p2[i])

    return result