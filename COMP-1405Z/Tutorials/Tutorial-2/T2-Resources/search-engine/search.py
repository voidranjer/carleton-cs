def main():

    # Initialization
    query = input("Enter a word to search for: ")
    max_count = 0
    max_count_page = "Not Found [ERROR]"
    max_ratio = 0
    max_ratio_page = "Not Found [ERROR]"

    pages_list = open("pages.txt", "r")
    for page in pages_list:
        filename = page.strip()

        # Count frequency (the second return value, _, is the total number of lines in the file (unused))
        freq, _ = count_frequency(filename, query)
        if (freq > max_count):
            max_count_page = filename
            max_count = freq

        # Count ratio
        ratio = count_ratio(filename, query)
        if (ratio > max_ratio):
            max_ratio_page = filename
            max_ratio = ratio

    pages_list.close()

    print(f"Max Page (Count): {max_count_page}")
    print(f"Max Count: {max_count}")
    print(f"Max Page (Ratio): {max_ratio_page}")
    print(f"Max Ratio: {max_ratio}")

def count_frequency(filename, query):
    """Counts the number of times a query string appears in the specified file.

    Args:
        filename (str): Name of file to search
        query (str): String to search in the specified file

    Returns:
        list: [Number of appearances, Total number of lines in the file]
    """
    line_count = 0
    freq = 0
    infile = open(filename, "r")

    for line in infile:
        line_count += 1
        if (line.strip() == query):
            freq += 1

    infile.close()
    return freq, line_count

def count_ratio(filename, query):
    """Counts the maximum word ratio of the specified word."""    
    freq, total_lines = count_frequency(filename, query)
    return (freq/total_lines)

if __name__ == "__main__":
    main()