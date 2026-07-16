"""
Program: Queue Implementation Using Arrays

Description:
Implements Queue Data Structure using Python arrays.
Supports Enqueue, Dequeue, Peek, Display,
Overflow and Underflow conditions.

Author: Bendram Swaranjith Reddy

Language: Python 3
"""

from array import array                     #<----->LINEAR QUEUE {using array}<----->
class queue:
    def __init__(self,size):
        self.size = size
        self.queue = array('i',[0]*size)
        self.rear = -1
        self.front = -1

    def enqueue(self,value):
        if self.rear == self.size-1:
            print("Queue Overflow!")
            return
        if self.front == -1:
            self.front = 0
            
        self.rear = self.rear+1
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow!")
            return
        x = self.queue[self.front]
        print("Deleted Element is:",x)
        self.front += 1

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Empty!")
            return
        print("Queue Elements are:")
        for i in range (self.front,self.rear+1):
            print(self.queue[i],end = " ")
        print()

#>--------------------->MENU-DRIVEN {PROGRAM}<--------------------->

q = queue(5)

while True:
    print("\n1-Enqueue")
    print("2-Dequeue")
    print("3-Display")
    print("4-Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting Program.....")
        break

    else:
        print("Invalid choice!")
