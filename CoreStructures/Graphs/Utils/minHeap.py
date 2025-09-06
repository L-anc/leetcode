from node import BinaryNode

# Finish later
class MinHeap:
    def __init__(self, node : BinaryNode):
        self.root = node

    def __firstLeaf(self) -> BinaryNode:
        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            cur = queue.pop(0)
            if (cur.left() or cur.right()) == None:
                return cur
            else:
                for child in cur.children():
                    queue.append(child)

        return None
    
    def __str__(self):
        
        
    def add(self, node : BinaryNode) -> None:
        leaf = self.__firstLeaf()

        if leaf.left() == None:
            leaf.setLeft(node)
        else:
            leaf.setRight(node)

        while node.parent() != None and node.value() < node.parent().value():
            parentNode = node.parent()
            pparent = parentNode.parent()
            if parentNode.left() == node:
                parentNode.left() = node.left()
            else:
                parentNode.right() = node.right()
                



        