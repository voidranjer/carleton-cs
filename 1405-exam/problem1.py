def median_word_length(filename):
    with open(filename, 'r') as infile:
        words = len(infile.read().split())
    return (words+1)/2
