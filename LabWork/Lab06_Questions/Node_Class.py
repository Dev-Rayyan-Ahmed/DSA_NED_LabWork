class Node:
    def __init__(self, item, next= None):
        self.item = item
        self.next = None
    
    def getItem(self):
        return self.item
    def getNext(self):
        return self.next
    def setItem(self, item):
        self.item = item
    def setNext(self, next):
        self.next = next