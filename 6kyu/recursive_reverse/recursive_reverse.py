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