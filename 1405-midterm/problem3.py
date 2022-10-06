ASS_WEIGHT = 25
MID_WEIGHT = 30
EXAM_WEIGHT = 45


def max_to_file(filename, ceiling):
    # Finds the max that is below the 'ceiling' value
    # Appends max to sorted.txt, in descending order (first line is the max, second line is next highest, etc)
    # Returns line number of max student (to be deleted) - also, the line starts from line 1, not 0
    # Returns -1 if the file is already empty

    outfile = open("sorted.txt", "a")
    with open(filename, "r") as infile:
        max_student_name = None
        second_max_student_name = None
        max_grade = -1

        buffer = infile.readline()
        while buffer != "":
            student_name = buffer.strip()
            grade = float(infile.readline().strip())
            if (grade > max_grade and grade < ceiling):
                max_grade = grade
                max_student_name = student_name
                second_max_student_name = None
            elif grade == max_grade and student_name != max_student_name:
                second_max_student_name = student_name

            buffer = infile.readline()

        if (max_grade != -1):
            outfile.write(max_student_name + " with grade " +
                          str(max_grade) + "\n")
            if (second_max_student_name != None):
                outfile.write(second_max_student_name + " with grade " +
                              str(max_grade) + "\n")

    outfile.close()
    return max_grade


def sort_to_file():
    # Expects a correctly formatted file "outfile.txt"

    # Resets sorted.txt output file (start appending to a clean sorted.txt file)
    with open("sorted.txt", "w") as outfile:
        outfile.write("")

    ceiling = 100
    ceiling = max_to_file("outfile.txt", ceiling)
    while ceiling != -1:
        return_value = max_to_file("outfile.txt", ceiling)
        if return_value < ceiling:
            ceiling = return_value


def print_sorted_grades(filename):

    infile = open(filename, "r")
    outfile = open("outfile.txt", "w")

    outfile.write("")  # Resets "outfile.txt"

    buffer = infile.readline()
    while buffer != "":
        first_name = buffer.strip()
        last_name = infile.readline().strip()
        student_number = infile.readline().strip()
        assignment_grade = float(infile.readline().strip())
        midterm_grade = float(infile.readline().strip())
        exam_grade = float(infile.readline().strip())
        buffer = infile.readline()

        final_grade = (assignment_grade*ASS_WEIGHT + midterm_grade*MID_WEIGHT +
                       exam_grade*EXAM_WEIGHT)/(ASS_WEIGHT+MID_WEIGHT+EXAM_WEIGHT)

        outfile.write(first_name + " " + last_name + "\n")
        outfile.write(str(final_grade) + "\n")

    infile.close()
    outfile.close()

    sort_to_file()

    with open("sorted.txt", "r") as infile:
        for line in infile:
            print(line.strip())


print_sorted_grades("studentinfo4.txt")
