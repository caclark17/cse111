def main():
    words_in_file = open("alice.txt", mode = "rt")
    
    d = num_word_count(words_in_file)

    sorted_words = sort_words(d)
    
    print(f"Total Word Count: {len(d.items())}")

    print(sorted_words)

def remove_punct(line):

    #Remove non-alphabet characters
    line = line.replace("`", "")
    line = line.replace(",", "")
    line = line.replace("-", "")
    line = line.replace(";", "")
    line = line.replace(".", "")
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("'", "")
    line = line.replace("?", "")
    line = line.replace("!", "")
    line = line.replace("\"", "")
    line = line.replace(":", "")

    return line


def num_word_count(words_in_file):

    d = dict()

    for line in words_in_file:
        #Remove the leading spaces and newline character
        line = line.strip()

        # Convert characters to lowercase
        line = line.lower()

        # Split the line into words
        words = line.split()

        for word in words:
        #Check if the word is already in dictionary

            word = remove_punct(word)
            
            if word in d:
                # Increment count of word by 1
                d[word] += 1

            else:
                # Add the word to the dictionary with count 1
                d[word] = 1

        return d

    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key,d[key] )

    print(d)

# Sort by highest value to lowest value
def sort_words(d):
    d_sorted = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return d_sorted



if __name__ == "__main__":
    main()