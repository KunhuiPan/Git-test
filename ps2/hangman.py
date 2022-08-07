# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for item in secret_word:
        if item not in letters_guessed:
            return False
        
    return True    
  



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    the_list = list()
    for item in list(secret_word):
        if item in letters_guessed:
            the_list.append(item)
        else:
            the_list.append("_ ")            
    
    guessed_letters =  "".join(str(i) for i in the_list)
    return guessed_letters
            



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    l = string.ascii_lowercase
    available_letters = list()
    for item in l:
        if item not in letters_guessed:
            available_letters.append(item)
    available_letters_left =  "".join(str(i) for i in available_letters)
    return available_letters_left
            
            
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # The user starts with 3 warnings & 6 guesses
    warnings = 3
    guesses = 6
    guessed_letters =list()
    
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is ", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left." )
    print("--------------------")

    
    while True:
        
        print("You have", guesses, "guesses left.")
        print("Available letters: ", get_available_letters(guessed_letters))
        
        str_letters = input("Please guess a letter: ").lower()
       
        # The user inputs anything beside an alphabet
        if str_letters.isalpha() == False:
           if warnings > 0:
               warnings -= 1
               print("Oops! This is not a valid letter. You had", warnings, "warnings left:", get_guessed_word(secret_word, guessed_letters))
               print("------------------")
           else:
               guesses -= 1
               print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:", get_guessed_word(secret_word, guessed_letters))
               print("------------------")
         
        # The user inputs an alphabet
        else:
            if str_letters in guessed_letters: # A letter has been guessed before
                if warnings > 0 :
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, guessed_letters))
                    print("------------------")
                else:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:",get_guessed_word(secret_word, guessed_letters))
                    print("------------------")
                    
        
            if str_letters not in guessed_letters: # A letter has not been guessed befor
                if str_letters in secret_word: # Guessing the right letter
                    guessed_letters.append(str_letters)
                    print("Good guess: ", get_guessed_word(secret_word, guessed_letters))
                    print("------------------") 
                    guesses -= 0

                else: # guessing wrong
                    guessed_letters.append(str_letters)
                    print("Oops! That letter is not in my word. Please guess a letter:", get_guessed_word(secret_word, guessed_letters))
                    print("------------------")
                    if str_letters in "aeiou" : # If guessing a vowel
                        guesses -= 2  
                    else: # If gussing a consonants           
                        guesses -= 1

       
        # Game over - win or lose, caculating game scores             
        if is_word_guessed(secret_word, guessed_letters):
            unique_letters_in_secret_word = list()
            for item in secret_word:
                if item not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(item)
            total_score = len(unique_letters_in_secret_word) * guesses
            
            print("Congratulations, you won!")           
            print("Your total score for this game is:", total_score)  
            break
        
        if guesses <= 0:
            print("Sorry, you ran out of guesses.The word was else.")
            break
           
   
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    myword_no_spece = my_word.replace(" ", "") #Remaining "_" spaces in my_word but delete white spaces.
    actual_letters = myword_no_spece.replace("_", "")
    return len(myword_no_spece) == len(other_word) and all ((a != '_' and a == b) or (a == '_' and b not in actual_letters) for a, b in zip(myword_no_spece, other_word))

        
                
            
            


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = list()
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
    
    if len(matches) == 0:
        return "No matches found"
    else:
        return " ".join(matches)

       
            

        
        
        
    
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses = 6
    guessed_letters =list()
    
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is ", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left." )
    print("--------------------")

    
    
    
    while True:
        
        print("You have", guesses, "guesses left.")
        print("Available letters: ", get_available_letters(guessed_letters))
        
        str_letters = input("Please guess a letter: ").lower()
       
        # The user inputs anything beside an alphabet
        if str_letters.isalpha() == False: 
            if str_letters == "*": 
                print("Possible word matches are:\n", show_possible_matches(get_guessed_word(secret_word, guessed_letters)))
                print("------------------")
            
            else:
                if warnings > 0:
                   warnings -= 1
                   print("Oops! This is not a valid letter. You had", warnings, "warnings left:", get_guessed_word(secret_word, guessed_letters))
                   print("------------------")
                else:
                   guesses -= 1
                   print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:", get_guessed_word(secret_word, guessed_letters))
                   print("------------------")
            
               
        # The user inputs an alphabet
        else:
            if str_letters in guessed_letters: # A letter has been guessed before
                if warnings > 0 :
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, guessed_letters))
                    print("------------------")
                else:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:",get_guessed_word(secret_word, guessed_letters))
                    print("------------------")
                    
        
            if str_letters not in guessed_letters: # A letter has not been guessed befor
                if str_letters in secret_word: # Guessing the right letter
                    guessed_letters.append(str_letters)
                    print("Good guess: ", get_guessed_word(secret_word, guessed_letters))
                    print("------------------") 
                    guesses -= 0

                else: # guessing wrong
                    guessed_letters.append(str_letters)
                    print("Oops! That letter is not in my word. Please guess a letter:", get_guessed_word(secret_word, guessed_letters))
                    print("------------------")
                    if str_letters in "aeiou" : # If guessing a vowel
                        guesses -= 2  
                    else: # If gussing a consonants           
                        guesses -= 1

       
        # Game over - win or lose, caculating game scores             
        if is_word_guessed(secret_word, guessed_letters):
            unique_letters_in_secret_word = list()
            for item in secret_word:
                if item not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(item)
            total_score = len(unique_letters_in_secret_word) * guesses
            
            print("Congratulations, you won!")           
            print("Your total score for this game is:", total_score)  
            break
        
        if guesses <= 0:
            print("Sorry, you ran out of guesses.The word was else.")
            break
        
        
    
    
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = "agile"
    #choose_word(wordlist)
    hangman_with_hints(secret_word)
