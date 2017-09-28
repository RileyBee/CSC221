'''
* 09/25/2017
*
* CSC 221
*
* Chris Noyes
*
* A game that allows the user to guess a randomly chosen number
* between 1 and 100.  The program returns too high, too low, or
* correct.
'''
def main():
    guessingGame()
   
        
def guessingGame():
    answer = 42  # Number to guess 
    numGuess = 0  # counter to track number of guesses it takes.
    low = 1  # start of range
    high = 100  # end of range
    guess = (high + low) / 2  #bisection formula 
        
    
    while (guess != answer): 
        numGuess += 1
        print('Low: ', low, 'High: ', high, 'Guesses', numGuess)
        
        
        if guess < answer:
            low = guess  # set low bound to guess value.
            
        
        else:
            high = guess  # set high bound to guess value            
    
        guess = (high + low) / 2 # keep bisecting.
    
    print('It took ', numGuess, 'guesses')
            
main()
