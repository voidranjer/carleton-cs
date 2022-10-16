# Dictionary format:
# - Key     = Element in list
# - Value   = Frequency of element in list

def addend(list, dict, value):
    list.append(value)
    if value not in dict:
        dict[value] = 0
    dict[value] += 1


def removestart(list, dict):
    if len(list) == 0:
        return None
    dict[list[0]] -= 1
    if dict[list[0]] == 0:
        del dict[list[0]]
    return list.pop(0)


def containslinear(list, value):
    return value in list


def containshash(dict, value):
    return value in dict
