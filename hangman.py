# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    a=list(secretWord)
    b=lettersGuessed
    if((set(a)&set(b))==set(a)):
        return True
    else:
        return False            
  
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      return example: '_ p p _ _'
    '''
    
    word=''
    for letter in secretWord:
        if letter not in lettersGuessed:
            word= word + '_ '
        else:
            word= word + letter + ' '
    print (word)
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    setA=list(string.ascii_lowercase)
    setB=(lettersGuessed)
    setC=set(setA) - set(setB)
    set_string=' '.join(setC)
    print("the remaining letters you dont have guessed")
    print(set_string)
    return(set_string)
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    '''

    lettersGuessed=[]
    for i in range(0,100):
        print("the length of word is {}".format(len(secretWord)))
        print("enter one character")
        
        
        lettersGuessed.append(input())
        
        test1=isWordGuessed(secretWord, lettersGuessed)
        
        if(test1==True):
            print("Congrats you won the game ")
            print("the WORD is \n{}".format(secretWord))
            break
        else:
            getGuessedWord(secretWord, lettersGuessed)
            
            getAvailableLetters(lettersGuessed)
           
        
    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
