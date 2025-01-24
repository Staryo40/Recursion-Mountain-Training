class ListNode:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = ListNode(head)
    
    def appendList(self, value):
        if (self.head == None):
            self.head = ListNode(value)
        else:
            currentNode = self.head
            if (currentNode.next == None):
                n = ListNode(value)
                currentNode.next = n
            else:
                currentNode.next.appendList(value)
    
    def prependList(self, value):
        if (self.head == None):
            self.head = ListNode(value)
        else:
            l = ListNode(value)
            l.next = self.head
            self.head = l

    def printList(self):
        if (self.head != None):
            currentNode = self.head
            if (currentNode.next != None):
                print(currentNode.info, end=" ")
                print("->", end=" ")
                nextNode = currentNode.next
                nextNode.printList()
            else:
                print(currentNode.info)
                

l = LinkedList(1)
l.printList()
l.appendList(2)
l.printList()
l.prependList(0)
l.printList()