class Node():
    def __init__(self,value=None,nxt = None):
        self.value = value
        self.next = nxt

def reverse(node:Node) -> Node:
    current = node
    nxt = None
    prevNode = None
    while current:
        nxt = current.next
        current.next = prevNode
        prevNode = current
        current = nxt
    return prevNode