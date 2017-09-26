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
import random

def main():
    guessingGame()
    
def guessingGame():
    rand = random.randint(1,100)
    guess = 0
    while guess != rand:
        guess = int(input("pick a number between 1 and 100: "))
        if guess < rand:
            print("too low")
        elif guess > rand:
            print("too high")            
        else:
            print("That's correct, great job!")
            
main()
