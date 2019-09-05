print ("Welcome to the game Spaceman!")
    player_name = input("What's your name? ")
    print('')
print("""Hello, "+player_name+". You are going to play the game Spaceman. 
      The program will pick a word at random from a list, and ask you to guess letters in the word. 
      After 5 wrong guesses, you lose the game. If you guess all of the letters 
      before you make 5 wrong guesses, you win the game.""")

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

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
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
        if letters not in letters_guessed:
            return False
        else:
            return True
            
    
    # ans = list(secret_word)
    # ans.pop()
    # return ans == letters_guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

#     #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet


# initialize an empty string 
    
    guessed_word = ""  
    
    # traverse in the string   
    for letters in secret_word:  
        if letters in letters_guessed
        guessed_word += letters + ""  
    
    # return string   
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
    
    
# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secret_word: string, the word the user is guessing
#     letters_guessed: list (of letters), which letters have been guessed so far
#     returns: string, comprised of letters, underscores (_), and spaces that represents
#       which letters in secret_word have been guessed so far.
#     '''
#     word_revealed = ""
#     for letter in secret_word:
#         if letter in letters_guessed:
#             word_revealed += letter
#         else:
#             word_revealed += "_ "
#     return word_revealed





def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    # there is a life support cable as part of the diagram of the Spaceman
    #you start with five lives
    #each time you lose a life, another part of the spaceman or his take off platform gets drawn    
    #you lose a life by guessing a letter that is not in the secret_word
    #before loop each time prints number of lives remaining
    #you win by guessing all of the letters in the secret word before you lose 5 lives
    # every round the program prints the list of letters not guessed, and the word_guessed, which is a combination of correct letters guessed and blank spaces
    #every round the program asks you for an input of a letter not yet guessed
    #while loop - loop game while game is not won or lost
        #print the word_guessed or letters_guessed
        #prompt user for a letter guess
        #call the function is_guess_in_word to determine whether the letter is in the word
        #tell the user if their guess is in the secret_word or not
            #update the letters_guessed
            #update the life total
            #update the word_guessed and print it
    

    #TODO: show the player information about the game according to the project spec
print ("Welcome to the game Spaceman!")
    player_name = input("What's your name? ")
    print('')
print("""Hello, "+player_name+". You are going to play the game Spaceman. 
      The program will pick a word at random from a list, and ask you to guess letters in the word. 
      After 5 wrong guesses, you lose the game. If you guess all of the letters 
      before you make 5 wrong guesses, you win the game.""")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
print("Guess ONE letter")
if guess == 

if len(guess) > 1:
    print ("Error: I said ONE letter you numpty!")
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
if guess 
    #TODO: show the guessed word so far
print word_guessed() 
    #TODO: check if the game has been won or lost


#this function starts the game
def test():
    print(secret_word)
    print(is_guess_in_word("x", "random")) #sets secret_word = "random", and "x" = letter guess


#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())