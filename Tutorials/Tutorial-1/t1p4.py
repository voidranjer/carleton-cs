def main():
    # colors allowed: ["green", "yellow", "red", others]
    color = input("Enter color of traffic light: ")
    distance = float(input("Enter distance to the intersection (in m): "))
    speed = float(input("Enter speed of car (in m/s): "))

    # speed = distance/time
    time = distance/speed

    if color == "green":
        print("Go")
    elif color == "yellow":
        # must reach in 5 seconds
        if time <= 5:
            print("Go")
        else:
            print("Stop")   
    elif color == "red":
        # must reach in 2 seconds
        if time <= 2:
            print("Go")
        else:
            print("Stop")   
    else:
        print("Stop")

if __name__ == "__main__":
    main()