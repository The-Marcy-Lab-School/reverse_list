class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def reverse(node: Node) -> Node:
    previous = None
    current = node
    nxt = None

    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    return previous