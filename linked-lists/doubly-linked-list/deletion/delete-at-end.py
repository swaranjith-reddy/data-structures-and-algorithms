class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll():
    def __init__(self):
        self.head=None

    def delete_end(self):
        if self.head is None:        # Empty list
            print("List empty!")
            return

        """if self.head.next is None:   # Only one node
            self.head = None
            return"""

        temp = self.head
        while temp.next is not None:             # Traverse to last node
            temp = temp.next
        temp.prev.next = None        # Previous node's next becomes None


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

l.delete_end()
print("After Deletion:")
l.display()
