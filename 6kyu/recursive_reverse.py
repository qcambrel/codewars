## Kata: Linked List - Recursive Reverse

# Linked Lists - Recursive Reverse

# Write a Recursive Reverse() function that recursively reverses a linked list. You may want to use a nested function for the recursive calls.

# var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
# reverse(list) === 5 -> 6 -> 3 -> 1 -> 2 -> null

class Node(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None

def reverse(head):
	current_node = head
	next_node = None
	previous_node = None
	while current_node:
		next_node = current_node.next
		current_node.next = previous_node
		previous_node = current_node
		current_node = next_node