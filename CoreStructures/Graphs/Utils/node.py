class Node:
    def __init__(self, value : int, children):
        self.val = value
        self.next = children
        self.prev = None

    def __str__(self):
        return f"Node(Val: {self.val}, Children: {self.next})"

    def value(self):
        return self.val

    def children(self):
        if self.next != None:
            return self.next
    
    def parent(self):
        return self.prev
    
class BinaryNode:
    def __init__(self, value : int):
        self.val = value
        self.leftNode = None
        self.rightNode = None
        self.prev = None
    
    def __init__(self, value : int, parent):
        self.val = value
        self.leftNode = None
        self.rightNode = None
        self.prev = parent

    def __str__(self):
        return f"Node(Val: {self.val}, Left: {self.leftNode}, Right: {self.rightNode})"

    def value(self):
        return self.val

    def left(self):
        return self.leftNode
    
    def setLeft(self, newLeft):
        self.leftNode = newLeft
        newLeft.prev = self
    
    def right(self):
        return self.rightNode

    def setRight(self, newRight):
        self.rightNode = newRight
        newRight.prev = self
    
    def parent(self):
        return self.prev

    def children(self):
        arr = []
        if self.leftNode != None:
            arr.append(self.leftNode)
        if self.rightNode != None:
            arr.append(self.rightNode)
        return arr
        

        
