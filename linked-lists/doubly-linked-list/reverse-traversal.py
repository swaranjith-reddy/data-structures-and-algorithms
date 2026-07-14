class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll():
    def __init__(self):
        self.head=None

    def display_reverse(self):
        if self.head is None:
            print("List empty!")
            return

        temp = self.head

        # Step 1: Go to last node
        while temp.next is not None:
            temp = temp.next

        # Step 2: Traverse backward
        while temp is not None:
            print(temp.data, end="<-->")
            temp = temp.prev
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
l.display_reverse()
 
