# https://www.codewars.com/kata/53ea07c9247bc3fcaa00084d

def look_and_say(data='1', maxlen=5):
    list = []
    list.append(helper_look(data))
    for i in range(maxlen-1):
        list.append(helper_look(list[-1]))

    return list

def helper_look(data):
    curentItem = data[0]

    final = ''
    counter = 1
    for i, item in enumerate(data[1:]):

        if item == curentItem:
            counter += 1
        else :
            final += str(counter) + curentItem
            curentItem = item
            counter = 1

    final += str(counter) + curentItem

    return final