"""Takes a string as input and return the pig latin equivalent."""


def main():
    """We will welcome the user, ask for a word, and then return
    the pig latin equivalent of that word.
    """
    print("Welcome to the Pig Latin Translator\n\n")
    english_string = input("What word would you like translated?\n\n")
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    pig_suffix = 'ay'
    new_ending = english_string[0]

    if english_string[0] in vowels:
        print("{} is translated as {}{}".format(english_string
                                              , english_string, pig_suffix))
    else:
        print("{} is translated as {}{}{}".format(english_string
                                              , english_string[1:]
                                              , new_ending, pig_suffix))


if __name__ == "__main__":
    main()

