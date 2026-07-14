class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    def __init__(self):
        self.head = None

    def delete_begin(self):
        if self.head is None:
            print("List is Empty! Nothing to delete.")
            return
        self.head = self.head.next   # Move head to next node

    def display(self):
        if self.head is None:
            print("List Empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


#  Create list
l = Sll()

n = Node(10)
n1 = Node(20)
n2 = Node(30)

l.head = n
n.next = n1
n1.next = n2

print("Before Deletion:")
l.display()

#  Delete at Beginning
l.delete_begin()

print("After Deletion at Beginning:")
l.display()
