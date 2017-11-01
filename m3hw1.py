# -*- coding: utf-8 -*-
"""
10/30/2017
CSC221 - M3HW1
@author: Chris Noyes

Exercise 1: Stack class

Exercise 2: Queue class
"""

class Stack(object):
    
    """
    A class to illustrate list stacks
    """
    
    #Accessor methods
    
    def __init__(self):
        
        self.item = []
        
    def __len__(self):
        
        return len(self.item)
    
    def __str__(self):
        
        return str(self.item)  
    
    
    # Mutator methods      
        
    def push(self, litem):
        
        self.item.append(litem)
        
    def pop(self):
        
        self.item.pop()
        
class Queue(object):
    
    """
    A class to illustrate list queues
    """
    
    #Accessor methods
    
    def __init__(self):
        
        self.item = []
        
    def __len__(self):
        
        return len(self.item)
    
    def __str__(self):
        
        return str(self.item)  
    
    
    # Mutator methods      
        
    def add(self, litem):
        
        self.item.insert(0,litem)
        
    def remove(self):
        
        self.item.pop()
        
        
def testStack():
    """Test Stack Class"""

    stck = Stack()
    
    print('Adding values to stack...')
    stck.push(5)
    stck.push(4)
    stck.push(1)
    print('Current list length: ', stck.__len__())
    print('Current list values: ', stck)
    print('*' * 31)
    print('Removing values from stack...')
    stck.pop()    
    stck.pop()
    stck.pop()
    print('Current list length: ', stck.__len__())
    print('Current list values: ', stck)

def testQueue():
    """ Test Queue Class"""

    q = Queue()
    
    print('Queueing...')
    q.add('first')
    q.add('second')
    q.add('third')
    print('Current queue length: ', q.__len__())
    print('Current queue members: ', q)  
    print('*' * 31)
    print('Dequeuing...')
    q.remove()
    print('Remaining in queue',q)
    q.remove()
    print('Remaining in queue',q) 
    q.remove() 
    print('Current queue length: ', q.__len__())
    print('Current queue members: ', q)     


        
    





    
