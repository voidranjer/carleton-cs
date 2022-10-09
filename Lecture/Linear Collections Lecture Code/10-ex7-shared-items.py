#Create a function that takes two lists as input. The function should return the number of items in the second list that appear in the first list.


#return True if item is in alist, False otherwise
def contains(alist, item):
    for i in alist:
        if i == item:
            return True
    return False

def count_same(list1, list2):
    count = 0
    for i in list2:
        #if i in list1:
        if contains(list1, i):
            count += 1
    return count

print(count_same([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8, 10]))
print(count_same([0, 1, 5, 7, 8, 2, 3, 9, 10], [0, 2, 4, 6, 8, 10]))
