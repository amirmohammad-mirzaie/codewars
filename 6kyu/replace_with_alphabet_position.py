# https://www.codewars.com/kata/546f922b54af40e1e90001da

import re
def alphabet_position(text):
    processed = ''.join(re.findall("[a-zA-Z]", text))

    a = ''
    for item in processed:
        if ord(item)<96:
            a += str(ord(item)-64) + ' '
        else:
            a += str(ord(item)-96) + ' '
    return a[:-1]