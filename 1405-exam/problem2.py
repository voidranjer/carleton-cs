def count(list1, list2):
    count = 0

    for item in list2:
        if item in list1:
            count += 1
            list1.remove(item)

    return count
