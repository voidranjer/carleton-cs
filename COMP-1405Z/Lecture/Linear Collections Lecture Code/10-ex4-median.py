#Write a function that uses the previously developed list sorting function to calculate the median value of a given list.

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

def median(alist):
    sorted = sort(alist)
    #repeat until the lenght of the list is 1 or 2:
        #given some sorted list
        #remove the lowest number
        #remove the highest number
    while len(sorted) > 2:
        sorted.pop(0)
        sorted.pop(len(sorted)-1)

    if len(sorted) == 1:
        return sorted[0]

    return (sorted[0] + sorted[1])/2

def median2(alist):
    sorted = sort(alist)
    if len(sorted) % 2 == 0: #even length list
        first = len(sorted)//2
        second = (len(sorted)//2) - 1
        median = (sorted[first] + sorted[second]) / 2
        return median
    else: #odd length list
        return sorted[(len(sorted)//2)]


list1 = [0,5,6,3,4,7,2,1] #3.5
list2 = [0,1,2,3,4,5,6,7,8] #4

print(median2(list1))
print(median2(list2))
