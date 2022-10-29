def find_largest_distance(filename):
    coords = []
    with open(filename, "r") as infile:
        infile.readline()
        for index, line in enumerate(infile):
            if index % 3 == 0:
                x = line.strip()
            elif (index - 1) % 3 == 0:
                y = line.strip()
                coords.append([int(x), int(y)])

    max_dist = 0
    for index in range(len(coords)):
        for compare_index in range(index, len(coords)):
            dist = abs(coords[index][0] - coords[compare_index][0]) + \
                abs(coords[index][1] - coords[compare_index][1])
            if dist > max_dist:
                max_dist = dist

    return max_dist
