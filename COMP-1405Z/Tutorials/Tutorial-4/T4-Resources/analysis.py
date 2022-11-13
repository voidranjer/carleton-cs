words = []

# Checks if a list is a subset of the "words" list
def is_subset(list):
    for item in list:
        if item not in words:
            return False
    return True

# Finds the highest frequency word given a dictionary with the structure of { word: frequency }
def find_max(word_freq_dict):
    max_freq = -1
    max_word = ""

    for word in word_freq_dict:
        if word_freq_dict[word] > max_freq:
            max_freq = word_freq_dict[word]
            max_word = word

    return max_word

# Converts an uncounted list to a dictionary with the structure of { word: frequency }
def list_to_dict(search_list, source_list):
    word_freq = {word: 0 for word in search_list}
    
    for search_word in search_list:
        for source_word in source_list:
            if source_word == search_word:
                word_freq[search_word] += 1
    return word_freq

def find_followed_words(str):
    results = []

    should_append = False
    for word in words:
        if(should_append):
            results.append(word)
            should_append = False
        if word == str:
            should_append = True
    return results    

def load(str):
    global words
    words = []
    with open(str, "r") as infile:
        for word in infile.read().split(" "):
            word = word.strip()
            if (len(word) > 0):
                words.append(word)

def commonword(list):
    if ((len(list) == 0) or (not is_subset(list))):
        return None

    return find_max(list_to_dict(list, words))


def commonpair(str):
    followed_words = find_followed_words(str)

    if len(followed_words) == 0:
        return None

    return find_max(list_to_dict(followed_words, followed_words))

def countall():
    return len(words)

def countunique():
    return len(list_to_dict(words, words))