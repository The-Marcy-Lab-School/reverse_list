class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

def reverse(node):
    curr = node
    prev = None
    nxt = None
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev