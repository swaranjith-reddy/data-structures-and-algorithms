"""
Program: Queue Implementation Using Linked Lists

Description:
Implements Queue Data Structure using Python Linked Lists.
Supports Enqueue, Dequeue, Peek, Display,
Underflow conditions.

Author: Bendram Swaranjith Reddy

Language: Python 3
"""

class Node:
    def __init__(self,data):        #<----->LINEAR QUEUE {using list}<----->
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new = Node(data)
        if self.front is None:
            self.front = new
            self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow!")
            return
        print("Deleted Element is:",self.front.data)
        self.front = self.front.next

        if self.front is None:   # 🔥 IMPORTANT FIX
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue Empty!")
            return
        temp = self.front
        while temp is not None:
            print(temp.data, end = "-->")
            temp =temp.next
        print(None)

#>--------------------->MENU-DRIVEN {PROGRAM}<--------------------->

q = Queue()

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
