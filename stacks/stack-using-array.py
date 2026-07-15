"""
Program: Stack Implementation Using Arrays

Description:
Implements Stack Data Structure using Python arrays.
Supports Push, Pop, Peek, Display,
Overflow and Underflow conditions.

Author: Bendram Swaranjith Reddy

Language: Python 3
"""

from array import array
class Stack:
    def __init__(self,size):
        self.size=size
        self.stack=array('i',[0]*size)
        self.top=-1

    #Add an element to the top of the stack    
    def push(self,value):
        if self.isfull():
            print("Stack Overflow")
        else:
            self.top+=1
            self.stack[self.top]=value

    #Check if the stack is full        
    def isfull(self):
        if self.top>=self.size-1:
            return True
        else:
            return False

    #Return the top element of the stack without removing it            
    def peek(self):
        if self.top==-1:
            print("Stack empty!")
            return
        print("The Top Element is:",self.stack[self.top])
    
    #Remove the top element from the stack and return it
    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return
        value = self.stack[self.top]
        self.top -= 1
        return value

    #Check if the stack is empty        
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False

    #Display all the elements in the stack    
    def display(self):
        if self.top==-1:
            print("The stack is empty!")
        else:
            print("Stack Elements are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])


s = Stack(5)

while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peek")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        s.peek()

    elif choice == 5:
        break

    else:
        print("Invalid choice!")
