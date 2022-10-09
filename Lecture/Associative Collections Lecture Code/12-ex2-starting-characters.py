#Write a program that reads the contents of a file and prints the letter that starts the most unique words.


#read the words from a file
#count up the frequency with which each letter starts a word
#find the letter with the highest frequency (the one that starts the most words

filein = open("positivewords.txt", "r")
freqs = {} #key -> the first character of the word, value -> how many times it started a word
words = {} #key -> first character, value -> a list of words that start with that char

for word in filein:
    word = word.strip()
    start_letter = word[0]

    if start_letter in words:
        if word in words[start_letter]:
            continue

    #start_letter is NOT in freqs
    if start_letter not in freqs:
        freqs[start_letter] = 1
        words[start_letter] = [word]
    #start_letter IS in freqs
    else:
        freqs[start_letter] = freqs[start_letter] + 1
        words[start_letter].append(word)


highest_freq = -1
highest_char = ""
for start in freqs:
    if freqs[start] > highest_freq:
        highest_freq = freqs[start]
        highest_char = start
print(highest_char, highest_freq)
