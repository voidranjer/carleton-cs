def average(inlist):
    return sum(inlist) / len(inlist)


def coldest_interval(alist, x):
    if len(alist) == x:
        return average(alist)

    averages = []

    index = 0
    while True:
        if (index + x) > len(alist):
            break

        interval = []
        for i in range(x):
            interval.append(alist[index + i])
        averages.append(average(interval))
        index += 1

    return min(averages)
