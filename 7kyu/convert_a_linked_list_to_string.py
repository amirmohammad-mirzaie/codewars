# https://www.codewars.com/kata/582c297e56373f0426000098

def stringify(node):
    st = ''
    while node:
        st = st + str(node.data) + ' -> '
        node = node.next
    st = st + 'None'
    return st
