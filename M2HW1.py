'''
* 10/1/2017
*
* CSC 221
*
* Chris Noyes
*
* Option A:
* Accepts string from user and returns any vowels found.
*
* Option B:
* Displays list of directions forward and in reverse.
*
* Option C:
* 
'''

def main():
    print('*' * 31)
    print('Select a program to run:')
    print ('A: Vowel Finder')
    print ('B: Driving Directions')
    print ('C: Customer Service Simulator')
    print('*' * 31)

    option = input('Enter Choice: ')
    print('*' * 31)
    
    if option == 'A':
        vowelFinder()
        
    elif option == 'B':
        drivingDirections()
        
    elif option == 'C':
        customers()
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
            
    print('*' * 31)
    print('The following vowels were found: ')
    print(tmp)
    print('*' * 31)
    
    
    
    
def drivingDirections():
    directions = ['Turn right onto Otis F. Jones Pkwy',
                  'Slight left onto Bow St',
                  'Turn right onto Green St',
                  'Turn left onto Barrington Cross St',
                  'Turn right onto Hull Rd']
    fwd = []

    print('Directions to school.')
    print('*' * 31)   
   
    for i in directions:
        print(i)
        fwd.append(i)

   
    print('*' * 31)
    print('Now let\'s see that in reverse!')
    print('*' * 31)
    
    while len(directions) > 0:
        print(directions.pop())
        
def customers():
    
    queue = ['Alice','Bob','Charles','Dennis','Elise','Fred','George']
    minute = ['5','10','15','20','25','30']
    
    for i in minute:        
        for j in queue:
            print('Now serving: ',queue.pop,
            



    

   
                
        
    
    
       
    
        
    
    
           
        
                                                    
main()
