class BinaryTree:
    def __init__(self, info=None, left=None, right=None):
        self.info = info
        self.left:BinaryTree = left
        self.right:BinaryTree = right
    
    def isEmpty(self):
        return (self.info == None)

    def isLeaf(self):
        return (self.info != None and self.right == None and self.left == None)
    
    def isUnerLeft(self):
        return (self.info != None and self.right == None and self.left != None)
    
    def isUnerRight(self):
        return (self.info != None and self.right != None and self.left == None)
    
    def isBinary(self):
        return (self.info != None and self.right != None and self.left != None)
    
    def depth(self):
        if (self.isEmpty()):
            return -1
        if (self.isLeaf()):
            return 0
        left = 0
        right = 0
        if (self.isUnerLeft()):
            left = 1 + self.left.depth()
        if (self.isUnerRight()):
            right = 1 + self.right.depth()
        return max(left, right)

    def level(self, value):
        # value is guaranteed to be on the tree
        if (self.info == value):
            return 0
        left = 0
        right = 0
        if (self.isUnerLeft()):
            left = 1 + self.left.level()
        if (self.isUnerRight()):
            right = 1 + self.right.level()
        return max(left, right)
    
    def printPreOrderList(self):
        if (not self.isEmpty()):
            if (self.isLeaf()):
                print(self.info)
            else:
                print(self.info, end="")
                if (self.isUnerLeft()):
                    self.left.printPreOrderList()
                elif (self.isUnerRight()):
                    self.right.printPreOrderList()
                else:
                    self.left.printPreOrderList()
                    self.right.printPreOrderList()
        
    def printInOrderList(self):
        if (not self.isEmpty()):
            if (self.isLeaf()):
                print(self.info)
            else:
                if (self.isUnerLeft()):
                    self.left.printPreOrderList()
                    print(self.info, end="")
                elif (self.isUnerRight()):
                    print(self.info, end="")
                    self.right.printPreOrderList()
                else:
                    self.left.printPreOrderList()
                    print(self.info, end="")
                    self.right.printPreOrderList()
    
    def printPostOrderList(self):
        if (not self.isEmpty()):
            if (self.isLeaf()):
                print(self.info)
            else:
                if (self.isUnerLeft()):
                    self.left.printPreOrderList()
                    print(self.info, end="")
                elif (self.isUnerRight()):
                    self.right.printPreOrderList()
                    print(self.info, end="")
                else:
                    self.left.printPreOrderList()
                    self.right.printPreOrderList()
                    print(self.info, end="")