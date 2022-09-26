words_in_file = open("alice.txt", mode = "rt")

def main():

    word_dict = dict()

    for words in words_in_file:
        words = words.rstrip()
            
        all_words = words.split()
            
        for individual_words in all_words:
                print(individual_words)

    return word_dict

main()