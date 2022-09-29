infile = open("salesinfo0.txt", "r")

lines = infile.readlines()
for i in range(0, len(lines), 6):
    print(lines[i].strip())

infile.close()