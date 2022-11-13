#Write a program that takes a filename and an integer x. The program should output the frequency of the x most common words in the filename.


#count the frequencies of all words
#find the X highest frequencies
#   How can we do that?
#   Find the highest frequency
#   Print and then remove that highest frequency
#   Repeat that process X times


filename = "14-rotk.txt"
x = 50

filein = open(filename, "r", encoding="latin")
words = filein.read().split(" ")

freqs = {} #key -> word, value -> frequency of word

for word in words:
    word = word.strip().lower().replace(".","").replace(",","").replace(";","")
    if len(word) == 0:
        continue

    if word not in freqs:
        freqs[word] = 0
    freqs[word] += 1


for i in range(x):
    highest_freq = -1
    highest_word = ""
    for word in freqs:
        if freqs[word] > highest_freq:
            highest_freq = freqs[word]
            highest_word = word
    print(highest_word, freqs[highest_word])
    del freqs[highest_word]
