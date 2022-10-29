def average(inlist):
    return sum(inlist) / len(inlist)


def coldest_interval(alist, x):
    counter = 0
    temps = []
    temp_intervals = []

    # This is to ensure that the last 'x' items in 'alist' is always included in the for loop
    # alist.extend([None for _ in range(x)])

    if len(alist) == x:
        return average(alist)

    for temp in alist:
        if counter < x:
            temps.append(temp)
        else:
            temp_intervals.append(temps)
            counter = 0
            temps = [temp]
        counter += 1

    if len(alist) % x != 0:
        temp_intervals.append(alist[-x:])

    return min([average(temps) for temps in temp_intervals])
