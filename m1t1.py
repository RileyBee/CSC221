def main():
    printMenu()

def printMenu():
    print('MARK V ADDINATOR ONLINE')
    print ('A: ADD')
    print ('B: ADD MORE')
    print ('C: GAME')

    option = input('MAKE SELECTION: ')    
    
    
    if option == 'A':
        intOne = int(input('Please enter first number '))
        intTwo = int(input('Please enter second number '))
        sumOne = int(intOne) + int(intTwo)
        print('SUM: ' , sumOne)
        again = input('AGAIN?' + ('' * 20) + '(Y/N)')
        if again == 'Y':
            printMenu()
        else:
            print('THANK YOU FOR USING THE MARK V ADDINATOR!')
            print('BE SURE TO PRE-ORDER THE MARK VI AT MATHSTOP TODAY!')
            exit()
            
    elif option == 'B':
        print('COMING SOON!')
        again = input('AGAIN?' + '(Y/N)')
        if again == 'Y':
            printMenu()
        else:
            exit()

    elif option == 'C':
        print('THIS FEATURE IS AVAILABLE TO PREORDER CUSTOMERS ONLY')
        printMenu()
        

    else:
            print('Only A, B, or C are accepted inputs')
            printMenu()
   
    
     
main()

