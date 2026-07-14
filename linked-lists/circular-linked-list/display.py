class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Cll:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        if self.head is None:
            print("List Empty!")
            return
        else:
            temp=self.head
            print(temp.data,end="-->")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,end="-->")
            print(temp.next.data)

l=Cll()
n1=Node(10)
l.head=n1
l.tail=n1
l.tail.next=l.head
print("After first node:")
l.display()
n2=Node(20)
l.tail.next=n2
l.tail=n2
l.tail.next=l.head
print("After second node:")
l.display()
n3=Node(30)
l.tail.next=n3
l.tail=n3
l.tail.next=l.head
print("After third node:")
l.display()
