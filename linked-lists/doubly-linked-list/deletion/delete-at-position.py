class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll():
    def __init__(self):
        self.head=None

    """def delete_pos(self, pos):
        if self.head is None:
            print("List Empty!")
            return

    # Case 1: Delete first node
        if pos == 1:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        temp = self.head
        for i in range(1, pos):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

    # Fix links
        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next"""

    #DELETE BY VALUE

    def delete_by_value(self, target_value):
        # Edge Case 1: Empty list
        if self.head is None:
            print("List is empty!")
            return

        temp = self.head

        # Edge Case 2: The target is the very first node (Head)
        if temp.data == target_value:
            self.head = temp.next  # Move the anchor
            if self.head is not None:
                self.head.prev = None  # Sever the backward tie
            return

        # The Engine: Search for the value
        while temp is not None and temp.data != target_value:
            temp = temp.next

        # Edge Case 3: We hit the end of the list and didn't find the value
        """if temp is None:
            print("Value not found!")
            return"""

        # The Splice: We found it in the middle or at the end
        # 1. Route the backward traffic forward
        if temp.prev is not None:
            temp.prev.next = temp.next
            
        # 2. Route the forward traffic backward (if it's not the last node)
        if temp.next is not None:
            temp.next.prev = temp.prev

    def display(self):
        if self.head is None:
            print("List Empty!")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end="<-->")
            temp=temp.next
        print("None")

l=Dll()
n=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
l.head=n
n.prev=None
n.next=n1
n1.prev=n
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
print("Before Deletion:")
l.display()

#l.delete_pos(2)
l.delete_by_value(30)
print("After Deletion:")
l.display()
