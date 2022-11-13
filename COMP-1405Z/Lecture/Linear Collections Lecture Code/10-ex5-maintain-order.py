#Write a program that maintains a sorted list of numbers the user enters. The user may enter the numbers in any order (i.e., not sorted). When the user enters “q”, the program should print out the median of the numbers.

numbers = []
number = input("Enter a number (q to quit): ")

while number != "q":
    number = int(number)

    #can we find the right index to add this number at
    #alist.insert(index, element)

    [0, 4, 7, 9, 11, 13]
    #for each index in the list:
    #   if the value we are entering is less than the value at this index
    #       insert the number at this index and stop
    added = False
    for i in range(len(numbers)):
        if number < numbers[i]:
            numbers.insert(i, number)
            added = True
            break
    if added == False:
        numbers.append(number)

    print(numbers)
    number = input("Enter a number (q to quit): ")
