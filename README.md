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
        #update the letters_guessed
                #print a list of letters that is a string. 
                each time a letter is guessed, remove from string, 
                    and add to word_guessed if it is correct. 
                    If not correct, reduce life total. 
            #update the life total
            #update the word_guessed and print it
            #update whether the game it won or lost

variables: 
    life total
    correct letters guessed
    letters not guessed 
    guessed_word (combination of secret word and )
