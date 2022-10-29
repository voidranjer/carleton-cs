def selection_sort(inlist):
    for index in range(len(inlist)):
        min_index = index
        for j_index in range(index + 1, len(inlist)):
            if inlist[j_index] > inlist[min_index]:
                min_index = j_index
        temp = inlist[index]
        inlist[index] = inlist[min_index]
        inlist[min_index] = temp

    return inlist


def most_common_color(filename):
    colors = {}
    with open(filename, "r") as infile:
        for _ in range(3):
            infile.readline()
        for index, color in enumerate(infile):
            color = color.strip()
            if index % 5 == 0:
                if color not in colors:
                    colors[color] = 1
                else:
                    colors[color] += 1
    return max(colors, key=colors.get)


def sorted_prices(filename):
    with open(filename, "r") as infile:
        prices = []
        counter = price = 0

        for _ in range(5):
            line = infile.readline()

        while line != "":
            if counter % 5 == 0:
                price = int(line.strip())
            if (counter - 1) % 5 == 0:
                if line.strip() == 'true':
                    prices.append(price)
            counter += 1
            line = infile.readline().strip()

    return selection_sort(prices)


print(sorted_prices('autoshow-example.txt'))
