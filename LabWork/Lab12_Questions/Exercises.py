class Tree:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

    def PRE_traverse(self):
        print(self.root, end= " ")
        if self.left is not None:
            self.left.PRE_traverse()
        if self.right is not None:
            self.right.PRE_traverse()
        
def TreeSize(root):
    count = 1
    if root.left is not None:
        count += TreeSize(root.left)
    if root.right is not None:
        count += TreeSize(root.right)
    return count

tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.right.left = Tree(6)
tree.right.right = Tree(7)

print("Filled Tree PREOrder-Traversal")
tree.PRE_traverse()
print("\nTree Size is: ",TreeSize(tree))

def ClearTree(tree):
    tree.root = 0
    if tree.left is not None:
        ClearTree(tree.left)
    if tree.right is not None:
        ClearTree(tree.right)

ClearTree(tree)
print("\nTree After Clearing All Values")
tree.PRE_traverse()

def DoubleOrderTraversal(tree):
    print(tree.root, end=" ")
    if tree.left is not None:
        DoubleOrderTraversal(tree.left)
    print(tree.root, end=" ")
    if tree.right is not None:
        DoubleOrderTraversal(tree.right)

tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
print("\nDouble Order Traversal")
DoubleOrderTraversal(tree)


