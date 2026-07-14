class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__ (self):
        self.head=None

    """def insert_at_position(self, pos, data):
        # Edge Case 1: Invalid position
        if pos < 1:
            print("Invalid position!")
            return

        new_node = Node(data)

        # Edge Case 2: Inserting at the very beginning (Position 1)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        
        # The Engine: Travel to the node exactly BEFORE the target position
        # We also check `temp is not None` to prevent crashing if pos is too large
        for i in range(1, pos - 1):
            if temp is None:
                print("Position out of bounds!")
                return
            temp = temp.next

        # Edge Case 3: We finished the loop, but temp fell off the edge
        if temp is None:
            print("Position out of bounds!")
            return

        # The Splice (You got this part right)
        new_node.next = temp.next
        temp.next = new_node"""
    
    def insert_pos(self, pos,data):
        new=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new

    def display(self):
        if self.head is None:
            print("List Empty!")
            return
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

# object creation
l = Sll()

n = Node(10)
n1 = Node(20)
n2 = Node(30)

l.head = n
n.next = n1
n1.next = n2

print("Before Insertion:")
l.display()

l.insert_pos(2,15)

print("After Insertion:")
l.display()
