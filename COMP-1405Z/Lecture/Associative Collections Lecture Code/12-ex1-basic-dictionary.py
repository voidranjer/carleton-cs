#Write a program that allows a user to do the following:
#1. Specify a key/value pair to save
#2. Ask for a value associated with a key
#3. Print all key/value pairs that have been saved
#4. Remove a key/value pair


d = {}

def get_command():
    print()
    print("The dictionary is currently: " + str(d))
    print()
    print("1. Specify a key/value pair to save")
    print("2. Ask for a value associated with a key")
    print("3. Print all key/value pairs that have been saved")
    print("4. Remove a key/value pair")
    print("5. Quit")
    return int(input("Enter a choice: "))


command = get_command()
while command != 5:
    if command == 1:
        #what if we never want to REPLACE the value associated with a key?
        print("Save a key/value pair.")
        key = input("Enter the new key: ")
        value = input("Enter the value associated with that key: ")

        if key in d:
            print("Cannot add duplicate key.")
        else:
            d[key] = value
            print("Added", key, value)
    elif command == 2:
        print("Retrieve a value for a key")
        key = input("Enter the key to get the value for: ")
        if key in d:
            print("The value associated with that is ", d[key])
        else:
            print("That key does not exist.")
    elif command == 3:
        print("Print all the key/value pairs")
        for key in d:
            print(key, d[key])
    elif command == 4:
        print("Remove a key/value pair")
        key = input("Enter the key to get rid of: ")
        if key in d:
            del d[key]
        else:
            print("That key does not exist.")
    else:
        print("Unknown command.")

    print(d)
    command = get_command()
