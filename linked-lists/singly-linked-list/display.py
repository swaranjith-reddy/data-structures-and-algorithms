class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("List Empty!")
        temp=self.head
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

l=Sll()
n=Node(10)
n1=Node(20)
n2=Node(30)
l.head=n
n.next=n1
n1.next=n2
l.display()
