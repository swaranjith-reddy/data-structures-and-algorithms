"""
Program: Circular Queue Implementation Using Linked lists

Description:
Implements Queue Data Structure using Python Lists.
Supports Enqueue, Dequeue, Peek, Display,
Underflow conditions.

Author: Bendram Swaranjith Reddy

Language: Python 3
"""

class Node:
    def __init__(self, data):              #<----->CIRCULAR QUEUE {using list}<----->
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)

        # FIRST NODE
        if self.front is None:
            self.front = new
            self.rear = new
            self.rear.next = self.front   #  circular link
            return

        # NORMAL INSERT
        self.rear.next = new
        self.rear = new
        self.rear.next = self.front   #  maintain circular link

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow!")
            return

        # ONLY ONE NODE
        if self.front == self.rear:
            print("Deleted Element:", self.front.data)
            self.front = None
            self.rear = None
            return

        # NORMAL DELETE
        print("Deleted Element:", self.front.data)
        self.front = self.front.next
        self.rear.next = self.front   #  maintain circular link

    def display(self):
        if self.front is None:
            print("Queue Empty!")
            return

        temp = self.front
        while True:
            print(temp.data, end="-->")
            temp = temp.next
            if temp == self.front:
                break
        print("(back to front)")


# ---------------- MENU DRIVEN ----------------

q = CircularQueue()

while True:
    print("\n1-Enqueue")
    print("2-Dequeue")
    print("3-Display")
    print("4-Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice!")