#Write a function that takes an unsorted list of numbers and returns a new list of the same numbers in sorted order (you may modify the lists).


#append
#remove an element
#remove from an index
#access at an index
#clear

def sort(unsorted):
    #go through unsorted, find smallest number
    #append smallest number to result list
    #remove smallest from the unsorted list
    #repeat that process until the unsorted list is empty
    result = []

    while len(unsorted) > 0:
        smallest = unsorted[0]
        for i in range(len(unsorted)):
            if unsorted[i] < smallest:
                smallest = unsorted[i]
        result.append(smallest)
        unsorted.remove(smallest)

    return result

x = [8, 4, 1, 9, 2, 7, 6, 3, 5]
print("Unsorted: " + str(x))
print("Sorted: " + str(sort(x)))
