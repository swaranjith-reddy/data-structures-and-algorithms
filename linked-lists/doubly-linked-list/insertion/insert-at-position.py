class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll():
    def __init__(self):
        self.head=None

    def insert_pos(self,pos,data):
        new=Node(data)
        temp=self.head
        for i in range (1,pos-1):
            temp=temp.next
        new.next=temp.next
        #new.prev=temp
        temp.next.prev=new
        temp.next=new

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
print("Before Insertion:")
l.display()

l.insert_pos(2,15)
print("After Insertion:")
l.display()
