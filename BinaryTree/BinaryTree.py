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
    
    def deleteTree(self):
        self.info = None
        self.right = None
        self.left = None
    
    def deleteLeft(self):
        self.left = None

    def deleteRight(self):
        self.right = None

    def deleteBranches(self):
        self.deleteLeft()
        self.deleteRight()

    def printPreOrder(self):
        if (not self.isEmpty()):
            print(self.info)
        
        print("L: ", end="")
        if (self.isUnerLeft()):
            self.printPreOrder(self.left)
        
        print("R: ", end="")
        if (self.isUnerRight()):
            self.printPreOrder(self.right)
        
    def printInOrder(self):
        pass

    def printPostOrder(self):
        pass