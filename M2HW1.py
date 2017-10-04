'''
* 10/1/2017
*
* CSC 221
*
* Chris Noyes
*
* Accepts string from user and returns any vowels found.
'''

def main():
    print('Select a program to run:')
    print ('A: Vowel Finder')
    print ('B: Driving Directions')
    print ('C: Customer Service Simulator')

    option = input('Enter Choice: ') 
    
    if option == 'A':
        vowelFinder()
        
    elif option == 'B':
        drivingDirections()
        
    elif option == 'C':
        print('coming soon')
    else:
        print('Only A, B, or C are accepted inputs')
        main()
        
    
def vowelFinder():
    phrase = input("Please enter phrase: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    tmp = []
    
    for chars in phrase:
        if chars in vowels:
            tmp.append(chars)
    
    print('The following vowels were found', tmp)
    
    
    
def drivingDirections():
    directions = ['Turn right onto Otis F. Jones Pkwy',
                  'Slight left onto Bow St',
                  'Turn right onto Green St',
                  'Turn left onto Barrington Cross St',
                  'Turn right onto Hull Rd']
        
    
   
#    for i in directions:
#        print(i)
    
    for i in directions:
        print(directions.pop())
        
        
    
    
       
    
        
    
    
           
        
    
    
    
    
    
    
    
    
    

    
    
    
    
main()