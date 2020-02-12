class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(node: Node) -> Node:
    prev = None
    curr = node
    ahead = curr.next 
    
    while curr:
        ahead = curr.next
        curr.next = prev
        prev = curr 
        curr = ahead
    return prev
        
    