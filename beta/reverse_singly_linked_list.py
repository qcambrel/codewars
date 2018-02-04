## Kata: Reverse a singly-linked list

# Implement a function reverse_list which takes a singly-linked list of nodes and returns a matching list in the reverse order.

# Assume the presense of a class Node, which exposes the property next. next must either be set to the next Node in the list, or to None to indicate the end of the list.

# To assist in writing tests, a function make_linked_list has also been defined, which converts a python list to a linked list of Node.

# The final tests will use a very long list. Be aware that a recursive solution will run out of stack.

def reverse_list(node):
	values = []
	while node:
		values.append(node.value)
		node = node.next
	values.reverse()
	return make_linked_list(values)

if __name__ == "__main__":
	assert reverse_list(Node(1, Node(2, Node(3, None)))) == Node(3, Node(2, Node(1, None)))
	assert reverse_list(make_linked_list([1, 2, 3, 4, 5])) == make_linked_list([5, 4, 3, 2, 1])