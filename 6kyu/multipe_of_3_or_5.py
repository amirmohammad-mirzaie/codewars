# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    third = (number-1)//3
    fifth = (number-1)//5
    fifteen = (number-1)//15

    final_third = third * (third+1)/2 * 3
    final_fifth = fifth * (fifth+1)/2 * 5
    final_fifteen = fifteen * (fifteen+1)/2 * 15

    value = final_fifth + final_third - final_fifteen

    return int(value)