class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    def __init__(self):
        self.head = None

    def delete_end(self):
        if self.head is None:
            print("List is Empty! Nothing to delete.")
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None   # Remove last node

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

#  Delete at End
l.delete_end()

print("After Deletion at End:")
l.display()
