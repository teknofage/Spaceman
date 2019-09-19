import random
from pygame import mixer #found on https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python

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
            guessed_word += "_"
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
            Your Spaceman is repelling Space Pirates, and is attached to the ship by 
            a life support cable. If the life support cable were to be severed by one 
            of the laser cannons they are dodging, they would be blasted off into space.
            
            The program will pick a word at random from a list, and ask you to guess letters in the word. 
            After 7 wrong guesses, you lose all 7 lives, and you lose the game. If you guess all of the letters 
            before you make 7 wrong guesses, you win the game. It is recommended that you choose to enjoy 
            both outcomes.""")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    lives = 7 #states that the number of lives is 7
    letters_guessed = [] # calls function and makes it an empty list
    guessed_word = "" #initialise guessed_word string
    while lives > 0 and not is_word_guessed(secret_word, letters_guessed):
        guessed_word = get_guessed_word(secret_word, letters_guessed) #guessed_word assigns a string, making the local variable available in this function, get_guessed_word creates the string made up of the two arguments
        print (guessed_word) #TODO: show the guessed word so far
        guess = input("Guess ONE letter: ")
        if len(guess) > 1: # checks if guess is more than one character
            lives == lives
            print (f"Error: I said ONE letter you numpty! You have {lives} lives left before you are blasted into space. ")
        if not guess.isalpha(): #checks if guess is an alphabetic letter
            lives == lives
            print (f"Major Error! Check that you know what a letter is before proceeding. You have {lives} lives left before you are blasted into space. ")
        #TODO: Check if the guessed letter is in the secret_word or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            letters_guessed.append(guess)
            print (f"Correct. You have {lives} lives left. Guess another letter. Letters already guessed: {letters_guessed}")
        elif not guess.isalpha() or len(guess) > 1 or guess in letters_guessed: #checks whether guess is not alphabetic, is longer than one character, or if it has been guessed already
            lives = lives #update lives variable 
        else:
            letters_guessed.append(guess)
            lives -= 1 #update lives variable 
            print (f"You've been hit! You have {lives} lives left before you are blasted into space. Letters already guessed: {letters_guessed}") #tells user how close they are to losing
        #TODO: check if the game has been won or lost
    if lives < 1:
        mixer.init()
        mixer.music.load('Babylon Zoo - Spaceman (Radio Edit).mp3')
        mixer.music.play()#plays "Spaceman" by Babylon Zoo
        return input (f"""You have lost the game. As a consequence of you failing to guess >{secret_word}<, 
        your spaceman has been blasted loose and is spiralling off into space. 
                      But we only need spacemen who can spell, because, once we escape the Space Pirates, 
                      this mission is to go to the Intergalactic Spelling Bee Championships on Mars. 
                      
                      Would you like to try again? Y/N""")
    elif is_word_guessed(secret_word, letters_guessed):
        return input (f"""Congratulations! You have correctly guessed >{secret_word}<, and won the game. 
                Your Spaceman has survived... this time.
                      
                                Would you like to play again? Y/N: """)


#this function starts the game
# def test():
#     #print(secret_word)
#     print(is_guess_in_word("x", "random")) #sets secret_word = "random", and "x" = letter guess

#Test Functions

def test_is_word_guessed():
    assert is_word_guessed(('story'),['s', 't', 'o', 'r', 'y']) is True
    assert is_word_guessed(('walking'),['w', 'a', 'l', 'k', 'i','n', 'g']) is True
    assert is_word_guessed(('snorkel'),['s', 'n', 'o', 'r', 'k', 'e', 'l']) is True


def test_is_guess_in_word():
    assert is_guess_in_word(("s"), ("string")) is True
    assert is_guess_in_word(("w"), ("winking")) is True
    assert is_guess_in_word(("p"), ("parable")) is True

def test_get_guessed_word():
    assert get_guessed_word(("balance"), ["b", "a", "l"]) == "bala___"
    assert get_guessed_word(("wilful"), ["f", "i", "l", "u" ]) == "_ilful"
    assert get_guessed_word(("crunchy"), ["r", "c", "h"]) == "cr__ch_"


#These function calls that will start the game
if __name__ == '__main__':
    while spaceman(load_word()).lower()[0] == "y": #David used this line of code to teach me how to combine these two lines and make the program loop
        pass
    #  print "_"

