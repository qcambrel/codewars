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
