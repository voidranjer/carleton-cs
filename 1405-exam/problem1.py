def selection_sort(inlist):
    for index in range(len(inlist)):
        min_index = index
        for j_index in range(index + 1, len(inlist)):
            if inlist[j_index] < inlist[min_index]:
                min_index = j_index
        temp = inlist[index]
        inlist[index] = inlist[min_index]
        inlist[min_index] = temp

    return inlist


def median_word_length(filename):
    with open(filename, 'r') as infile:
        lengths = selection_sort([len(word) for word in infile.read().split()])

        if len(lengths) % 2 != 0:
            return lengths[len(lengths)//2]
        return (lengths[len(lengths) // 2 - 1] + lengths[len(lengths)//2]) / 2
