class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


def insert(root,key):

    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)

    return root


def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def delete(root,key):

    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left,key)

    elif key > root.key:
        root.right = delete(root.right,key)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.key = temp.key

        root.right = delete(root.right,temp.key)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)



# Main Program

root = None

values = [50,30,70,20,40,60,80]

for v in values:
    root = insert(root,v)

print("Inorder before deletion:")
inorder(root)

root = delete(root,20)
root = delete(root,30)

print("\nInorder after deletion:")
inorder(root)
