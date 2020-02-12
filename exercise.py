class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
        
def reverse(node):
    current = node
    prev = None
    nxt = None 
    
    while current != None:
        nxt = current.next
        current.next = prev
        prev = current 
        current = nxt
    return prev
    
    