class Node:
    def __init_(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        
        while node in not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


