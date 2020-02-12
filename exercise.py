class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        
    def __iter__(self):
        pass

def reverse(node: Node) -> Node: #Takes Node object, return Node ->

    current = node
    prev = None
    ahead = None
    nxt = None
    
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
        

# iterate through entire Linked List
# Assign prev to data of previous Node upon Each iteration.
#

