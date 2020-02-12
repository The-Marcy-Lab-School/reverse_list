class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(node: Node) -> Node:
    prev = None
    curr = node
    ahead = curr.next 
    
    while curr:
        curr.next = prev
        prev = curr 
        curr = ahead
        ahead = curr.next
        
    