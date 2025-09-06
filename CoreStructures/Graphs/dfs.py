from Utils.node import Node

def dfs(node : Node, target : int):
    if node.val == target:
        return node

    for child in node.next:
        resNode = dfs(child, target)
        if resNode != None:
            return resNode
    
    return None

# testTree = Node(5, [Node(7, [Node(6, []), Node(2, [])]), Node(3, [Node(10, []), Node(15, [])])])
# node = dfs(testTree, 15)
# print(node)
# print(node.val)