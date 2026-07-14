class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Cll:
    def __init__(self):
        self.head=None
        self.tail=None

    """def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None"""

    def delete_pos(self,pos):
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        temp.next = temp.next.next


    """def delete_pos(self, pos):
        if self.head is None:
            print("List Empty!")
            return

        # Delete first node
        if pos == 1:
            self.delete_begin()
            return

        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
            if temp == self.tail:
                print("Invalid Position!")
                return

        del_node = temp.next
        temp.next = del_node.next

        if del_node == self.tail:
            self.tail = temp"""

    
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
print("After Deletion:")
l.delete_pos(3)
l.display()

