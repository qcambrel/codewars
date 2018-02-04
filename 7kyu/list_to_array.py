## Kata: List to Array

# Lists are data structures composed of nested objects, each containing a single value and a reference to the next object.

# Here's an example of a list in JavaScript:

# {value: 1, next: {value: 2, next: {value: 3, next: null}}}
# In Python, lists will be represented by a preloaded LinkedList class with the members value and next. Here's an example:

# LinkedList(1, LinkedList(2, LinkedList(3)))
# Write a function listToArray (or list_to_array in Python) that converts a list to an array, like this:

# [1, 2, 3]
# Assume all inputs are valid lists with at least one value. For the purpose of simplicity, all values will be either numbers, strings, or Booleans.

def list_to_array(lst):
	array = [lst.value]
	while lst.next:
		lst = lst.next
		array.append(lst.value)
	return array


if __name__ == "__main__":
	assert list_to_array(LinkedList(1)) == [1]
	assert list_to_array(LinkedList(4, LinkedList(25, LinkedList(30)))) == [4, 25, 30]
	assert list_to_array(LinkedList(2, LinkedList(40, LinkedList(43, LinkedList(25, LinkedList(125)))))) == [2, 40, 43, 25, 125]
