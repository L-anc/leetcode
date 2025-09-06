from Utils.node import Node

def bfs(node : Node, target : int):
    queue = []
    queue.append(node)

    while len(queue) > 0:
        cur = queue.pop(0)
        print(cur.val)
        if cur.val == target:
            return cur
        else:
            for child in cur.next:
                queue.append(child)

    return None
        

# testTree = Node(5, [Node(7, [Node(6, []), Node(2, [])]), Node(3, [Node(10, []), Node(15, [])])])
# node = bfs(testTree, 2)
# print(node)
# print(node.val)