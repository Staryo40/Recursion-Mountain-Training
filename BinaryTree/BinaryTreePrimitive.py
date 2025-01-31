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
                print(self.info, end="")
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
                print(self.info, end="")
            else:
                if (self.isUnerLeft()):
                    self.left.printInOrderList()
                    print(self.info, end="")
                elif (self.isUnerRight()):
                    print(self.info, end="")
                    self.right.printInOrderList()
                else:
                    self.left.printInOrderList()
                    print(self.info, end="")
                    self.right.printInOrderList()
    
    def printPostOrderList(self):
        if (not self.isEmpty()):
            if (self.isLeaf()):
                print(self.info, end="")
            else:
                if (self.isUnerLeft()):
                    self.left.printPostOrderList()
                    print(self.info, end="")
                elif (self.isUnerRight()):
                    self.right.printPostOrderList()
                    print(self.info, end="")
                else:
                    self.left.printPostOrderList()
                    self.right.printPostOrderList()
                    print(self.info, end="")

    def printLeavesLR(self):
        if (self.isLeaf()):
            print(self.info)
        else:
            if (self.isUnerLeft()):
                self.left.printLeavesLR()
            if (self.isUnerRight()):
                self.right.printLeavesLR()
            if (self.isBinary()):
                self.left.printLeavesLR()
                self.right.printLeavesLR()

    # print plan
    # 1. make a matrix dimension = depth*(2^(depth)-1)
    # 2. basis is the lowest level (leaf), has space between each leaf of 2^1 - 1 or 1
    # 3. the next level follows the rule of space between nodes are 2^(depth-level+1) - 1 and the space at the outer nodes are from the space between nodes of the lower level