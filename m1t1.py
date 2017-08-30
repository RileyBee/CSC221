def main():
    printMenu()

def printMenu():
    print('MARK V ADDINATOR ONLINE')
    print ('A: ADD')
    print ('B: ADD MORE')
    print ('C: GAME')

    option = input('MAKE SELECTION: ')    
    
    
    if option == 'A':
        intOne = int(input('FIRST NUMBER? '))
        intTwo = int(input('SECOND NUMBER? '))
        sumOne = int(intOne) + int(intTwo)
        print('SUM: ' , sumOne)
        again = input('AGAIN?' + '(Y/N)')
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

