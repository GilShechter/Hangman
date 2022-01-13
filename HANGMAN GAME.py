# By: Gil Shechter


def opening_screen():
    #This functions prints the opening screen of Hangman game.
    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ /                      
                        |___/"""
    print(HANGMAN_ASCII_ART)					
    MAX_TRIES = 6					 
    print("You have", MAX_TRIES, "tries")

HANGMAN_PHOTOS = { #this dictionary contains the 7 situations of the hangman.
"0": \
"    x-------x",
"1": \
"""    x-------x
    |
    |
    |
    |
    |""",
"2":\
"""    x-------x
    |       |
    |       0
    |
    |
    |""",
"3": \
"""    x-------x
    |       |
    |       0
    |       |
    |
    |""",
"4": \
"""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
"5": \
"""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
"6": \
"""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

def choose_word(file_path, index):
    """This function gets a file path and an index number and returns the file's word in that index.
    :param file_path: file path string
    :param index: index value
    :type file_path: str
    :type index: str
    :return: the word in the file in the specific index.
    :rtype: str
    """
    with open(file_path, "r") as words_file:
        words = words_file.read()
        words_list = words.split(' ')
        words_index = int(index) % len(words_list)
        return words_list[words_index-1]

def game_board(secret_word):
    """This function gets a string and replaces each letter with "_".
    :param secret_word: string value
    :type secret_word: str
    :return: a string of "_ " * the number of letters in secret_word
    :rtype: str
    """
    return "_" * len(secret_word)

def show_hidden_word(secret_word, old_letters_guessed):
    """This function gets a string which is the word that the user needs to guess, and a list that contains the letters that he already guessed.
    The function returns a list that consists of letters and '_'.
    the string shows the word from old_letters_guessed that guessed correctly from  secret_word.
    :param secret_word: value of the string that the user needs to guess
    :param old_letters_guessed: list of the letters that already been guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: a new list with the correctly guessed letters
    :rtype: list
    """
    game_play = list(game_board(secret_word))
    for letter in old_letters_guessed:
        for letter_check in range(len(secret_word)):
            if letter == secret_word[letter_check]:
                game_play[letter_check] = letter
    return ' '.join(game_play)

def check_valid_input(letter_guessed, old_letters_guessed):
    """The function checks the validity of a given string.
    :param letter_guessed: a string
    :param old_letters_guessed: a list of string that has already been checked.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if letter_guessed is alphabetic, a single charachter, and haven't been used before. False otherwise.
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function check the validity of a given string. if valid, returns True and adds the string to old_letters_guessed.
    if not valid, returns 'False', and prints the list(sorted) and 'X'.
    :param letter_guessed: a string
    :param old_letters_guessed: a list of string that has already been checked.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if letter_guessed is valid. False if not valid.
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed += letter_guessed
        return True
    else: 
        old_letters_guessed.sort()
        print('X\n', ' -> '.join(old_letters_guessed), sep='')
        return False

def check_win(secret_word, old_letters_guessed):
    """This function gets a string and a list and check if all the characters of the string is in the list.
    :param secret_word: string value
    :param old_letters_guessed: list of strings
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True whether all the characters of the word is in the list, False if not.
    :rtype: bool
    """
    for letters in secret_word:
        if letters not in old_letters_guessed:
            return False
    return True

def hangman (old_letters_guessed, secret_word, num_of_tries):
    """This function runs the game. is gets the secret word, a list to append the guessed letters to,
    and a variable that counts the number of unsuccesful tries. The function gets a guessed letter from the user each time,
    checks if the input is valid, and prints the result.
    :param old_letters_guessed: a list of letters
    :param secret_word: secret_word value
    :param num_of_tries: num_of_tries value
    :type old_letters_guessed: list
    :type secret_word: str
    :type num_of_tries: int
    """
    while num_of_tries < 7:
        letter_guessed = input("Guess a letter: ")
        if try_update_letter_guessed(letter_guessed.lower(), old_letters_guessed) == True:
            if letter_guessed not in secret_word:
                num_of_tries += 1
                if num_of_tries != 6:
                    print(":(",  "\n", 6-num_of_tries, "more tries!")
        else:
            continue
        if check_win(secret_word, old_letters_guessed) == True:
            print(show_hidden_word(secret_word, old_letters_guessed), "\nWin")
            break
        if num_of_tries == 6:
            print("LOSE", "\nSorry, you have been hanged! The answer was:\n", secret_word)
            break
        print(HANGMAN_PHOTOS[str(num_of_tries)], '\n', show_hidden_word(secret_word, old_letters_guessed))

def play_again():
    """This function checks is the user wants to play again.
    :return: True if the user answers 'Y', False if not.
    :rtype: bool
    """
    play_again_choice = input("Type Y to play again ")
    if play_again_choice == "Y":
        return True
    else:
        print("Goodbye!")
        return False

def main():
    #Gets the file path and index from the user, calls the function choose_word to select the secret word, calls the function hangman to run the game.
    import os
    opening_screen()
    file_path = input("Please enter file path: ")
    while os.path.isfile(file_path) == False:
        print("File doesn't exist")
        file_path = input("Please enter file path: ")
    play_again_check = True
    while play_again_check == True: 
        index = input("Enter index: ")
        while index.isdigit() == False:
            print("You did not enter a number")
            index = input("Enter index: ")
        secret_word = choose_word(file_path, index)
        old_letters_guessed = []
        num_of_tries = 0
        print("Let's start!\n", HANGMAN_PHOTOS[str(num_of_tries)], '\n', show_hidden_word(secret_word, old_letters_guessed))
        hangman(old_letters_guessed, secret_word, num_of_tries)
        play_again_check = play_again()

if __name__ == "__main__":
    main()
