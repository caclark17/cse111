def main():
    words_in_file = open("alice.txt", mode = "rt")
    num_word_count(words_in_file)

def num_word_count(words_in_file):

    d = dict()

    for line in words_in_file:
        #Remove the leading spaces and newline character
        line = line.strip()

        # Convert characters to lowercase
        line = line.lower()

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

        # Split the line into words
        words = line.split()

        for word in words:
        #Check if the word is already in dictionary

            if word in d:
                # Increment count of word by 1
                d[word] += 1

            else:
                # Add the word to the dictionary with count 1
                d[word] = 1

    # Sort by highest value to lowest value
    sorted(d, key=d.get, reverse=True)

    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key,d[key] )

    print(d)

if __name__ == "__main__":
    main()