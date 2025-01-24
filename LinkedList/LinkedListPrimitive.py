class LinkedList:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next
    
    def appendList(self, value):
        if (self.info == None):
            self.info = value
        else:
            if (self.next == None):
                l = LinkedList(value)
                self.next = l
            else:
                self.next.appendList(value)
    
    def prependList(self, value):
        if (self.info == None):
            self.info = value
        else:
            l = LinkedList(self.info)
            l.next = self.next
            self.info = value
            self.next = l

    def printList(self):
        if (self.info != None):
            if (self.next != None):
                print(self.info, end=" ")
                print("->", end=" ")
                self.next.printList()
            else:
                print(self.info)
                

l = LinkedList(1)
l.printList()
l.appendList(2)
l.printList()
l.prependList(0)
l.printList()