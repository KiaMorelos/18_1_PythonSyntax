def print_upper_words(words, letters):
    """Pass in a list of words, and a list of letters that the word should start with. The loop iterates through each word and checks for a first letter match, and then prints in uppercase: HELLO, HEY"""

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
        # if word.startswith('e') or word.startswith('E'):
        #     print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "Eggs"], ["h", "y"])