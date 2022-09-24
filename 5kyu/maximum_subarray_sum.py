# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
def max_sequence(arr):
    global_max = float('-inf')
    current_max = float('-inf')
    for i in arr:
        current_max = max(current_max + i, i)
        global_max = max(current_max, global_max)

    if global_max != float('-inf') and global_max > 0:
        return global_max
    else:
        return 0