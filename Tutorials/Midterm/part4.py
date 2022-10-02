def largestvolume(filename):
    with open(filename, "r") as infile:
        largest_vol = 0

        while True:
            first_line = infile.readline()
            if first_line == "":
                break
            length = float(first_line.strip())
            width = float(infile.readline().strip())
            height = float(infile.readline().strip())
            
            volume = length*width*height

            if volume > largest_vol:
                largest_vol = volume
    
    return largest_vol