def analyze(filename):
    max_streak = 0

    with open(filename, "r") as infile:
        running_streak = 0
        for line in infile:
            num = int(line.strip())
            if (num % 2 == 0):
                if running_streak > max_streak:
                    max_streak = running_streak
                running_streak = 0
            else:
                running_streak += 1

        if running_streak > max_streak:
            return running_streak

    return max_streak
