# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    sortedList = []
    sortedWord = sorted(word)
    for item in words:
        if sorted(item) == sortedWord:
            sortedList.append(item)


    return sortedList