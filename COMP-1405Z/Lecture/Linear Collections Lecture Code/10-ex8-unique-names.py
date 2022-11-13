#Create a program that will store a list of names entered by the user. The list should never have any duplicate names.

names = []
name = input("Enter a name (q to quit): ")

while name != "q":
    if not (name in names):
        names.append(name)
    print(names)
    name = input("Enter a name (q to quit): ")
