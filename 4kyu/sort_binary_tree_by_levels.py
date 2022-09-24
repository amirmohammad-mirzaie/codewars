# https://www.codewars.com/kata/52bef5e3588c56132c0003bc

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


def helper(value_list:list, q:Queue):

    if q.q:
        node = q.pop()

        if node:
            value_list.append(node.value)
            q.insert(node.left)
            q.insert(node.right)

        helper(value_list, q)



    return value_list