def count(list1, list2):
    list2_index = counter = 0
    for char in list1:
        if char == list2[list2_index]:
            if list2_index == len(list2) - 1:
                list2_index == 0
                counter += 1
            else:
                list2_index += 1
        else:
            list2_index = 0

    return counter
