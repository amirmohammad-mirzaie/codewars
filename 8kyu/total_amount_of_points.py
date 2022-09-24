# https://www.codewars.com/kata/5bb904724c47249b10000131

def points(games):
    score = 0
    for item in games:
        result = extract_numbers(item)
        score += map(result)
    return score

def extract_numbers(string):
    a, b = str.split(string, ':')
    a = int(a)
    b = int(b)
    return (a, b)
def map(tuple):
    a, b = tuple
    if a > b:
        return 3
    elif a < b:
        return 0
    else:
        return 1