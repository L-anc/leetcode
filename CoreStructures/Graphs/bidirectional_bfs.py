from Utils.node import Node

def biDirectonalBfs(startNode : Node, endNode: Node):
    distance = 0
    queueStart = []
    queueStart.append(startNode)

    queueEnd = []
    queueEnd.append(endNode)

    while len(queueStart) and len(queueEnd) > 0:
        curStart = queueStart.pop(0)
        curEnd = queueEnd.pop
        distance += 1

        if curStart == curEnd:
            return distance
        else:
            for child in curStart.next:
                queueStart.append(child)

            for child in curEnd.next:
                queueEnd.append(child)

    return None