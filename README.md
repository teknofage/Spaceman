 # Welome to the game of Spaceman. It's like Hangman, but in space, and nobody gets hanged.
    # there is a life support cable as part of the diagram of the Spaceman, butyou can't see it. When you lose the game, the life support cabel is cut, and your Spaceman is blasted into space.
    #you start with seven lives
    #the program selects a secret word from a list
    #you lose a life by guessing a letter that is not in the secret_word
    #before loop each time prints number of lives remaining, and the guessed word updated with the correct letters guessed.
    #you win by guessing all of the letters in the secret word before you lose 7 lives
    #every round the program asks you for an input of a letter not yet guessed
    #while loop - loop game while game is not won or lost
        #print the word_guessed so far
        #prompt user for a letter guess
        #call the function is_guess_in_word to determine whether the letter is in the word
        #update the letters_guessed
                #print a list of letters that is a string. 
                each time a letter is guessed, remove from string, 
                    and add to word_guessed if it is correct. 
                    If not correct, reduce life total. 
            #update the life total
            #update the word_guessed and print it
            #update whether the game is won or lost

variables: 
    player_name
    secret_word
    guess
    letters
    lives
    letters_guessed
    words_list
    guessed_word (combination of secret word and )
