"""
Program: Circular Queue Implementation Using Arrays

Description:
Implements Queue Data Structure using Python arrays.
Supports Enqueue, Dequeue, Peek, Display,
Overflow and Underflow conditions.

Author: Bendram Swaranjith Reddy

Language: Python 3
"""

class CircularQueue:
    def __init__(self, size):                 #<----->CIRCULAR QUEUE {using arrays}<----->
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.isfull():
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        #print(data, "inserted")

    def dequeue(self):
        if self.isempty():
            print("Queue Underflow")
            return

        print("Deleted element:", self.queue[self.front])

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    #Check if the queue is empty
    def isempty(self):
        return self.front == -1

    #Check if the queue is full
    def isfull(self):
        return (self.rear + 1) % self.size == self.front

    #Display the elements of the queue
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Queue elements:")

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

#>--------------------->MENU-DRIVEN {PROGRAM}<--------------------->

q = CircularQueue(5)

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
