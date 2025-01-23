from BinaryTreePrimitive import *

def listToBST(l:list[int]) -> BinaryTree:
    tree = BinaryTree()
    for i in range(len(l)):
        insertToBST(tree, l[i])
    return tree

def insertToBST(t:BinaryTree, x:int):
    if (t.info == None):
        t.info = x
        return
    if (t.info > x):
        insertToBST(t.left, x)
    else:
        insertToBST(t.right, x)

