
# https://www.codewars.com/kata/56b5dc75d362eac53d000bc8
import re


def calculate_string(st):
    global ops, splitted, first_number, second_number
    op = re.findall(r'[\+\-*/]', st)[0]

    splitted = re.split('[*/\-+]', st)
    first_number = (re.sub("[^\d\.]", "", splitted[0]))
    second_number = (re.sub("[^\d\.]", "", splitted[1]))

    final_string = first_number + op + second_number
    return str(round(eval(final_string)))