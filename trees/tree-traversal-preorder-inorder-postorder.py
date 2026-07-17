class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self):
        self.root = Node(10)
        self.root.left = Node(20)
        self.root.right = Node(30)
        self.root.left.left = Node(40)
        self.root.left.right = Node(50)

    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

bt = BinaryTree()
bt.create()

print("Preorder Traversal:")
bt.preorder(bt.root)

print("\nInorder Traversal:")
bt.inorder(bt.root)

print("\nPostorder Traversal:")
bt.postorder(bt.root)
