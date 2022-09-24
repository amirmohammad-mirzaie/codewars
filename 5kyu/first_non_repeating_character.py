# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    #your code here
    dictionary = {}
    for i in string:
        if i.lower() in dictionary:
            dictionary[i.lower()] = 1
        else:
            dictionary[i.lower()] = 0

    chosen_char = ''
    for i in string:
        if dictionary[i.lower()]==0:
            chosen_char = i
            break
    return chosen_char
