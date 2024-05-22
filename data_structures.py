# arrays is list in python
array = [1, 2, 3, "four"]

# linked lists: A data structure where each element points to the next one, 
# forming a chain
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



