def main():
    calculator_art = """
     _____________________
    |  _________________  |
    | | JO           0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """

    # pointless decorations
    print(calculator_art)

    # main menu ui element
    print("--------------------------------------")
    print("           GRADE CALCULATOR           ")
    print("--------------------------------------")
    print("Main Menu:")
    print("[0] Calculate final grade (default weighting)")
    print("[1] Calculate final grade with custom weighting")
    print("[2] Exit")
    
    # user input
    choice = input("\nYour choice: ")

    if choice == "0":
        default_weight()
    elif choice == "1":
        custom_weight()
    elif choice == "2":
        print("\nExiting...")
    else:
        print("\nInvalid option! Exiting...")

# if user chooses to use the default weightings (20, 20, 20, 40)
def default_weight():
    MIDTERM_WEIGHT = 0.2
    FINAL_WEIGHT = 0.4

    midterm1 = float(input("\nInput % of 1st Midterm Test Score: "))
    midterm2 = float(input(r"Input % of 2nd Midterm Test Score: "))
    midterm3 = float(input(r"Input % of 3rd Midterm Test Score: "))

    final_score = float(input(r"Input % of Final Exam Score: "))

    print(f"\nYour final grade is: {round(MIDTERM_WEIGHT*(midterm1 + midterm2 + midterm3) + FINAL_WEIGHT*final_score, 3)} ")

# if user chooses to use their own custom weightings
def custom_weight():
    print("\n[MIDTERM 1]")
    midterm1 = float(input("Enter score (%): "))
    weight1 = float(input("Enter weight (%): "))

    print("\n[MIDTERM 2]")
    midterm2 = float(input("Enter score (%): "))
    weight2 = float(input("Enter weight (%): "))

    print("\n[MIDTERM 3]")
    midterm3 = float(input("Enter score (%): "))
    weight3 = float(input("Enter weight (%): "))

    print("\n[FINAL EXAM]")
    final_score = float(input("Enter score (%): "))
    final_weight = float(input("Enter weight (%): "))


    sum_of_weighted_scores = weight1*midterm1 + weight2*midterm2 + weight3*midterm3 + final_weight*final_score
    sum_of_weights = weight1+weight2+weight3+final_weight

    print(f"\nYour final grade is: {round(sum_of_weighted_scores/sum_of_weights, 3)}")

if __name__ == "__main__":
    main()