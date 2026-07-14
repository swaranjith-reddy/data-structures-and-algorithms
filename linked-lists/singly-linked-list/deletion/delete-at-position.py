class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    def __init__(self):
        self.head = None

    """def delete_at_position(self, pos):
        # Edge Case 1: Empty list
        if self.head is None:
            print("List is empty!")
            return

        # Edge Case 2: Deleting the very first node
        if pos == 1:
            self.head = self.head.next  # Move the anchor to the second node
            return

        temp = self.head

        # The Engine: Travel to the node EXACTLY BEFORE the target
        for i in range(1, pos - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds!")
                return
            temp = temp.next

        # Edge Case 3: We found the previous node, but the target node doesn't exist
        if temp.next is None:
            print("Position out of bounds!")
            return

        # The Bypass: Route the pointer AROUND the target node
        temp.next = temp.next.next"""

    def delete_pos(self, pos):
        if self.head is None:
            print("List is Empty!")
            return

        # If deleting first node
        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid Position!")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid Position!")
            return

        temp.next = temp.next.next   # Bypass the node

    def display(self):
        if self.head is None:
            print("List Empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


l = Sll()

n = Node(10)
n1 = Node(20)
n2 = Node(30)

l.head = n
n.next = n1
n1.next = n2

print("Before Deletion:")
l.display()

l.delete_pos(3)   # Delete node at position 3

print("After Deletion at Position 3:")
l.display()
