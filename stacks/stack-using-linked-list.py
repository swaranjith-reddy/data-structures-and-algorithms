"""
Program: Stack Implementation Using Linked List

Description:
Implements Stack Data Structure using Python linked lists.
Supports Push, Pop, Peek, Display,
Underflow condition.

Author: Bendram Swaranjith Reddy

Language: Python 3
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    #Push method to add an element to the top of the stack    
    def push(self,data):
        new=Node(data)
        if self.top is None:
            self.top=new
        else:
            new.next=self.top
            self.top=new

    #Peek method to view the top element of the stack without removing it        
    def peek(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("Top element is: ", self.top.data)

    #Pop method to remove the top element from the stack        
    def pop(self):
        if self.top is None:
            print("stack underflow")
        else:
            value=self.top.data
            print("The popped element is: ",value)
            self.top=self.top.next
            

    #Display method to show the elements in the stack        
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            temp=self.top
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next
            print("None")

    #Check if the stack is empty        
    def isempty(self):
        if self.top is None:
            return True
        else:
            return False

    #Check if the stack is full (not applicable for linked list implementation, but included for completeness)    
    def isfull(self):
        if self.top is None:
            return False
        

# -------- MENU DRIVEN PROGRAM --------

s = Stack()

while True:
    print("\nStack Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
