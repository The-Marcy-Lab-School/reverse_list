'''
P: Given a linked list, reverse it in place so the head node is now the tail node

E: See tests

D: Linked List,Node

A:


C:
'''
class Node:
    def __init__(self, data=None, Node = None):
        self.data = data
        self.next = Node
        
    def __repr__(self):
        return str(f"Node: {self.data}")



def reverse(node:Node) ->Node:
    current = node
    nxt = None
    previous = None
    
    while current:
        nxt = current.next
        
        current.next = previous
        
        previous = current
        
        current = nxt
        
    return previous   
        
        
        
        
        
        
        