# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2

import numpy as np

def check_portions(board):
    board = np.array(board)
    done = True
    for i in range(3):
        for j in range(3):

            start_row = 3 * i
            end_row = 3 * (i + 1)

            start_col = 3 * j
            end_col = 3 * (j + 1)

            portion = board[start_row:end_row, start_col:end_col]
            sett = set(portion.ravel())
            if len(sett) != 9:
                done = False
                break

    return done


def done_or_not(board):  # board[i][j]
    done = True
    for i in range(9):
        # row_sets.append(set(board[i]))
        if len(set(board[i])) != 9 or set(board[i]) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            done = False
            break

        temp_col = []
        for j in range(9):
            temp_col.append(board[j][i])
        if len(set(temp_col)) != 9 or set(temp_col) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            done = False
            break

        if done:
            done = check_portions(board)

    if done:
        return 'Finished!'
    else:
        return 'Try again!'
