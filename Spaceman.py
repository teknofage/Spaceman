import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    # print(secret_word)
    return secret_word
    

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letters in secret_word:
        if letters not in letters_guessed: #checks that the letters in secret_word are in letters_guessed
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
        Returns: string, comprised of letters, underscores (_), and spaces that represents
            which letters in secret_word have been guessed so far.
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

#     #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_word = ""
    
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters #loop through letters in secret_word and add correct guesses to guessed_word
        else: 
            guessed_word += "_ "
    return guessed_word



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False
    

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    print ("Welcome to the game Spaceman!")
    player_name = input("What's your name? ")
    print('')
    print(f"""Hello, {player_name}. You are going to play the game Spaceman. 
      The program will pick a word at random from a list, and ask you to guess letters in the word. 
      After 7 wrong guesses, you lose the game. If you guess all of the letters 
      before you make 7 wrong guesses, you win the game.""")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
# if guess == 
    lives = 7 #states that the number of lives is 7
    letters_guessed = [] # calls function and makes it an empty list
    guessed_word = get_guessed_word(secret_word, letters_guessed) #guessed_word assigns a string, making the local variable available in this function, get_guessed_word creates the string made up of the two arguments
    print (guessed_word) #TODO: show the guessed word so far
    guess = input("Guess ONE letter: ")
    if len(guess) > 1: # checks if guess is more than one character
        print ("Error: I said ONE letter you numpty!")
    if not guess.isalpha(): #checks if guess is an alphabetic letter
        print ("Major Error! Check that you know what a letter it before proceeding.")
    #TODO: Check if the guessed letter is in the secret_word or not and give the player feedback
    if is_guess_in_word(guess, secret_word):
        print (f"Correct. You have {lives} lives left. Guess another letter. ")
    else:
        lives -= 1 #update lives variable 
        print (f"You have {lives} lives left before you are blasted into space.") #tells user how close they are to losing
    #TODO: check if the game has been won or lost
    if lives < 1:
        print ("You have lost the game. Would you like to try again? Y/N")
    elif (guessed_word == secret_word):
        print ("You have won the game. Would you like to play again? Y/N")


#this function starts the game
def test():
    print(secret_word)
    print(is_guess_in_word("x", "random")) #sets secret_word = "random", and "x" = letter guess


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

#  print "_"