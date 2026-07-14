class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head=None

    def insert_end(self, data):  
        new = Node(data)  
        if self.head is None:  
            self.head = new  
            return  
        temp = self.head  
        while temp.next is not None:  
            temp = temp.next  
        temp.next = new

    def display(self):
        if self.head is None:
            print("List Empty!")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end='-->')
            temp=temp.next
        print("None")

l=Sll()
n=Node(10)
n1=Node(20)
n2=Node(30)
l.head=n
n.next=n1
n1.next=n2

print("Before Insertion:")
l.display()

l.insert_end(40)

print("After Insertion:")
l.display()
