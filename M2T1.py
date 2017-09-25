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
    guess = int(input("pick a number between 1 and 101: "))
    while guess != rand:
        if guess < rand:
            print("too low")
            guess = int(input("pick a number between 1 and 100: "))
        elif guess > rand:
            print("too high")
            guess = int(input("pick a number between 1 and 100: "))
        else:
            print("That's correct, great job!")
            
main()
