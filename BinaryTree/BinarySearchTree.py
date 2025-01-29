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
        if (t.left == None):
            new = BinaryTree(x)
            t.left = new
        else:
            insertToBST(t.left, x)
    else:
        if (t.right == None):
            new = BinaryTree(x)
            t.right = new
        else:
            insertToBST(t.right, x)

x = [3,1,6,9,5,7]
tree = listToBST(x)
# tree.printLeavesLR()
tree.printPreOrderList()
print("")
tree.printInOrderList()
print("")
tree.printPostOrderList()
print("")
