def reverse(st):
	words = st.split(" ")
	words.reverse()
	return (" ").join(words)

if __name__ == "__main__":
	assert reverse('Hello World') == 'World Hello'
	assert reverse('Hi There.') == 'There. Hi'