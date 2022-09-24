import sys

sys.setrecursionlimit(10000)


def spiralize(size):
    moving = MovingObj(size=size)
    moving.right(row_no=0, col_no=0)

    spiral = moving.board

    return spiral


class MovingObj:

    def __init__(self, size):
        self.size = size

        self.row_no = 0
        self.col_no = 0

        self.board = [[0 for x in range(self.size)] for y in range(self.size)]

    def right(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no][col_no - 1] = 0

                return

            if row_no == 0:
                self.board[row_no][col_no] = 1

                if col_no == (self.size - 1):
                    self.down(row_no + 1, col_no)
                else:
                    self.right(row_no, col_no + 1)

            elif self.board[row_no][col_no + 1] == 0:

                self.board[row_no][col_no] = 1
                self.right(row_no, col_no + 1)

            else:

                self.down(row_no + 1, col_no - 1)

    def left(self, row_no, col_no):
        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no][col_no + 1] = 0

                return

            if row_no == (self.size - 1):
                self.board[row_no][col_no] = 1

                if col_no == 0:
                    self.up(row_no - 1, col_no)
                else:
                    self.left(row_no, col_no - 1)

            elif self.board[row_no][col_no - 1] == 0:

                self.board[row_no][col_no] = 1
                self.left(row_no, col_no - 1)

            else:

                self.up(row_no - 1, col_no + 1)

    def up(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no + 1][col_no] = 0

                return

            if self.board[row_no - 1][col_no] == 0:

                self.board[row_no][col_no] = 1
                self.up(row_no - 1, col_no)

            else:

                self.right(row_no + 1, col_no + 1)

    def down(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no - 1][col_no] = 0

                return

            if col_no == (self.size - 1):
                self.board[row_no][col_no] = 1

                if row_no == (self.size - 1):
                    self.left(row_no, col_no - 1)
                else:
                    self.down(row_no + 1, col_no)

            elif self.board[row_no + 1][col_no] == 0:

                self.board[row_no][col_no] = 1
                self.down(row_no + 1, col_no)

            else:

                self.left(row_no - 1, col_no - 1)


5
months
agoRefactorDiscuss
import sys

sys.setrecursionlimit(10000)


def spiralize(size):
    moving = MovingObj(size=size)
    moving.right(row_no=0, col_no=0)

    spiral = moving.board

    return spiral


class MovingObj:

    def __init__(self, size):
        self.size = size

        self.row_no = 0
        self.col_no = 0

        # the # of y will create rows. the # of x will create columns
        self.board = [[0 for x in range(self.size)] for y in range(self.size)]

    def right(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no][col_no - 1] = 0

                return

            if row_no == 0:
                self.board[row_no][col_no] = 1

                if col_no == (self.size - 1):
                    self.down(row_no + 1, col_no)
                else:
                    self.right(row_no, col_no + 1)

            elif self.board[row_no][col_no + 1] == 0:

                self.board[row_no][col_no] = 1
                self.right(row_no, col_no + 1)

            else:

                self.down(row_no + 1, col_no - 1)

    def left(self, row_no, col_no):
        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no][col_no + 1] = 0

                return

            if row_no == (self.size - 1):
                self.board[row_no][col_no] = 1

                if col_no == 0:
                    self.up(row_no - 1, col_no)
                else:
                    self.left(row_no, col_no - 1)

            elif self.board[row_no][col_no - 1] == 0:

                self.board[row_no][col_no] = 1
                self.left(row_no, col_no - 1)

            else:

                self.up(row_no - 1, col_no + 1)

    def up(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no + 1][col_no] = 0

                return

            # if col_no == 0:
            #     self.board[col_no][row_no] = 1
            #     self.up(row_no - 1, col_no)

            # if row_no == 0:
            #     self.left(row_no, col_no-1)
            # else:
            #     self.down(row_no+1, col_no)

            if self.board[row_no - 1][col_no] == 0:

                self.board[row_no][col_no] = 1
                self.up(row_no - 1, col_no)

            else:

                self.right(row_no + 1, col_no + 1)

    def down(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no - 1][col_no] = 0

                return

            if col_no == (self.size - 1):
                self.board[row_no][col_no] = 1

                if row_no == (self.size - 1):
                    self.left(row_no, col_no - 1)
                else:
                    self.down(row_no + 1, col_no)

            elif self.board[row_no + 1][col_no] == 0:

                self.board[row_no][col_no] = 1
                self.down(row_no + 1, col_no)

            else:

                self.left(row_no - 1, col_no - 1)


5
months
agoRefactorDiscuss
4
kyu
Nesting
Structure
Comparison
Python:
import re


def same_structure_as(original, other):
    new_original = str(original).replace("'['", "x")
    new_original = new_original.replace("']'", "x")

    new_other = str(other).replace("'['", "x")
    new_other = new_other.replace("']'", "x")

    new_original = re.sub(r'-?\d+', 'x', new_original)
    new_other = re.sub(r'-?\d+', 'x', new_other)

    if new_original != new_other:
        return False
    return True


7
months
agoRefactorDiscuss
4
kyu
Sort
binary
tree
by
levels
Python:


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


class Queue:
    def __init__(self):
        self.q = []

    def insert(self, value):
        self.q.append(value)

    def pop(self):
        return self.q.pop(0)


def tree_by_levels(node):
    value_list = []
    q = Queue()
    q.insert(node)

    value_list = helper(value_list, q)
    return value_list


def helper(value_list: list, q: Queue):
    if q.q:
        node = q.pop()

        if node:
            value_list.append(node.value)
            q.insert(node.left)
            q.insert(node.right)

        helper(value_list, q)

    return value_list


2
years
agoRefactorDiscuss
5
kyu
Did
I
Finish
my
Sudoku?
Python:
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


2
years
agoRefactorDiscuss
5
kyu
Weight
for weight
    Python:


def sum_digits(num):
    summ = 0
    while num:
        summ += (num % 10)
        num = num // 10
    return summ


def order_weight(strng):
    # your code
    split = strng.split()
    split = sorted([(sum_digits(int(item)), item) for item in split])
    result = ' '.join(item[1] for item in split)

    return result


2
years
agoRefactorDiscuss
5
kyu
Scramblies
Python:
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


2
years
agoRefactorDiscuss
5
kyu
Maximum
subarray
sum
Python:


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


2
years
agoRefactorDiscuss
5
kyu
First
non - repeating
character
Python:


def first_non_repeating_letter(string):
    # your code here
    dictionary = {}
    for i in string:
        if i.lower() in dictionary:
            dictionary[i.lower()] = 1
        else:
            dictionary[i.lower()] = 0

    chosen_char = ''
    for i in string:
        if dictionary[i.lower()] == 0:
            chosen_char = i
            break
    return chosen_char


2
years
agoRefactorDiscuss
5
kyu
PaginationHelper
Python:


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page:
            return (len(self.collection) // self.items_per_page + 1)
        else:
            return (len(self.collection) // self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        unfinished_pages = self.has_unfinished_page()
        page_count = self.page_count()

        if page_index > (page_count - 1) or page_index < 0:
            return -1
        elif page_index == (page_count - 1):
            if not unfinished_pages:
                return self.items_per_page
            else:
                return len(self.collection) % self.items_per_page
        else:
            return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if (item_index > (len(self.collection) - 1)) or (item_index < 0):
            return -1

        return (item_index // self.items_per_page)

    def has_unfinished_page(self):
        if len(self.collection) % self.items_per_page:
            return True
        return False


2
years
agoRefactorDiscuss
7
kyu
Sum
of
a
sequence
Python:


def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0

    return begin_number + sequence_sum(begin_number + step, end_number, step)


2
years
agoRefactorDiscuss
5
kyu
Mean
without
outliers
Python:


def help_clean(sample, cutoff):
    isClean = True
    mean = sum(sample) / len(sample)
    power = [(item - mean) ** 2 for item in sample]
    sd = ((sum(power)) / (len(sample))) ** 0.5

    for item in (list(sample)):
        if (item > (mean + cutoff * sd)) or (item < (mean - cutoff * sd)):
            isClean = False
            sample.remove(item)
    if isClean:
        return mean

    return help_clean(sample, cutoff)


def clean_mean(sample, cutoff):
    return round(help_clean(sample, cutoff), 2)


2
years
agoRefactorDiscuss
7
kyu
Reverser
Python:


def help_reverse(n, b):
    while n // 10:
        r = n % 10
        b = b * 10 + r
        n = n // 10
    b = b * 10 + n
    return b


def reverse(n):
    b = 0
    reversedNumber = help_reverse(n, b)

    return reversedNumber


2
years
agoRefactorDiscuss
5
kyu
Where
my
anagrams
at?
Python:


def anagrams(word, words):
    sortedList = []
    sortedWord = sorted(word)
    for item in words:
        if sorted(item) == sortedWord:
            sortedList.append(item)

    return sortedList


2
years
agoRefactorDiscuss
7
kyu
nova
polynomial
1.
add
Python:


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


2
years
agoRefactorDiscuss
6
kyu
Bit
Counting
Python:


def countBits(n):
    list = []
    l = helpCount(n, list)
    return sum(l)


def helpCount(n, list):
    if n > 1:
        helpCount(n // 2, list)
    list.append(n % 2)
    return list


2
years
agoRefactorDiscuss
6
kyu
Replace
With
Alphabet
Position
Python:
import re


def alphabet_position(text):
    processed = ''.join(re.findall("[a-zA-Z]", text))

    a = ''
    for item in processed:
        if ord(item) < 96:
            a += str(ord(item) - 64) + ' '
        else:
            a += str(ord(item) - 96) + ' '
    return a[:-1]


2
years
agoRefactor
6
kyu
Look and say
numbers
Python:


def look_and_say(data='1', maxlen=5):
    list = []
    list.append(helper_look(data))
    for i in range(maxlen - 1):
        list.append(helper_look(list[-1]))

    return list


def helper_look(data):
    curentItem = data[0]

    final = ''
    counter = 1
    for i, item in enumerate(data[1:]):

        if item == curentItem:
            counter += 1
        else:
            final += str(counter) + curentItem
            curentItem = item
            counter = 1

    final += str(counter) + curentItem

    return final


2
years
agoRefactorDiscuss
7
kyu
Convert
a
linked
list
to
a
string
Python:


def stringify(node):
    st = ''
    while node:
        st = st + str(node.data) + ' -> '
        node = node.next
    st = st + 'None'
    return st


2
years
agoRefactorDiscuss
6
kyu
Multiples
of
3 or 5
Python:


def solution(number):
    third = (number - 1) // 3
    fifth = (number - 1) // 5
    fifteen = (number - 1) // 15

    final_third = third * (third + 1) / 2 * 3
    final_fifth = fifth * (fifth + 1) / 2 * 5
    final_fifteen = fifteen * (fifteen + 1) / 2 * 15

    value = final_fifth + final_third - final_fifteen

    return int(value)


2
years
agoRefactorDiscuss
6
kyu
Basics
03: Strings, Numbers and Calculation
Python:
import re


def calculate_string(st):
    global ops, splitted, first_number, second_number
    op = re.findall(r'[\+\-*/]', st)[0]

    splitted = re.split('[*/\-+]', st)
    first_number = (re.sub("[^\d\.]", "", splitted[0]))
    second_number = (re.sub("[^\d\.]", "", splitted[1]))

    final_string = first_number + op + second_number
    return str(round(eval(final_string)))


2
years
agoRefactorDiscuss
6
kyu
Convert
string
to
camel
case
Python:
import re


def to_camel_case(text):
    words = re.split('[_\-]', text)
    camels = words[0] + ''.join(w.capitalize() for w in words[1:])
    return camels


2
years
agoRefactorDiscuss
8
kyu
Total
amount
of
points
Python:


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


2
years
agoRefactorDiscuss
8
kyu
Multiply
Python:


def multiply(a, b):
    return a * b


3
years
agoRefactor
© 2022
CodewarsAboutAPIBlogPrivacyTermsContact
powered
by

