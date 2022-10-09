#Write a program that will ask the user for a filename, read the file, and then ask the user for a word W. The program should then print out each word W2 that follows W in the file and how many times W2 follows W.


filename = "14-rotk.txt"
filein = open(filename, "r", encoding="latin")
pre_words = filein.read().split(" ")
filein.close()

words = []
for word in pre_words:
    word = word.strip().lower().replace(".","").replace(",","").lower()
    if len(word) == 0:
        continue
    words.append(word)
    print(word)

#words -> a list of all the words in the text

#they -> did (9), went (5), jumped (11)
#freqs -> keys = word, value = frequency of that word

#outer dictionary: key -> word, value -> dictionary with frequencies of following words
#inner dictionary: key -> word that followed, how many times it followed

info = {}

for i in range(1, len(words)):
    prev_word = words[i-1]
    cur_word = words[i]

    if prev_word not in info:
        info[prev_word] = {}

    if cur_word not in info[prev_word]:
        info[prev_word][cur_word] = 0
    info[prev_word][cur_word] += 1

word = input("Enter the word you want to know about: ")

while word != "q":
    #print out all the following words for whatever 'word' variable is
    if word not in info:
        print("That word didn't occur anywhere.")
    else:
        follow_freqs = info[word]
        largest = -1
        largest_word = ""
        for key in follow_freqs:
            #print(key, follow_freqs[key])
            if follow_freqs[key] > largest:
                largest = follow_freqs[key]
                largest_word = key
        print(largest_word, largest)

    word = input("Enter the word you want to know about: ")
