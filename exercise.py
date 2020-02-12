class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

def reverse(l_head):
	prev = None
	current = l_head
	nxt = None

	while current:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt

	return prev