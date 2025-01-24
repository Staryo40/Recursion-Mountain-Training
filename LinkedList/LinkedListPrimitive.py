class LinkedList:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next
    
    def length(self):
        if (self.info == None):
            return 0
        if (self.next == None):
            return 1
        return 1 + self.next.length()

    def printList(self):
        if (self.info != None):
            if (self.next != None):
                print(self.info, end=" ")
                print("->", end=" ")
                self.next.printList()
            else:
                print(self.info)

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

    def insertAt(self, value, index):
        if (self.length() < index):
            print("Invalid index: index larger than list length")
        elif (index < 0):
            print("Invalid index: negative index")
        else:
            if (index == 0):
                self.prependList(value)
            else:
                if (index == 1):
                    l = LinkedList(value)
                    l.next = self.next
                    self.next = l
                else:
                    self.next.insertAt(value, index-1)

    def deleteFirst(self):
        value = self.info
        if (self.next == None):
            self.info = None
        else:
            if (self.next.next == None):
                secondLast = self
                secondLast.info = secondLast.next.info
                secondLast.next.info = None
                secondLast.next = None
            else:
                self.info = self.next.info
                self.next.deleteFirst()
        return value
    
    def deleteLast(self):
        if (self.next == None):
            value = self.info
            self.info = None
            return value
        else:
            if (self.next.next == None):
                secondLast = self
                value = secondLast.next.info
                secondLast.next.info = None
                secondLast.next = None
                return value
            else:
                return self.next.deleteLast()
                

l = LinkedList(1)
l.printList()
l.appendList(2)
l.printList()
l.prependList(0)
l.printList()
l.insertAt(7, 2)
l.printList()
l.deleteFirst()
l.printList()
x = l.deleteLast()
l.printList()
print(f"x value = {x}")
x = l.deleteLast()
l.printList()
print(f"x value = {x}")
x = l.deleteLast()
l.printList()
print(f"x value = {x}")