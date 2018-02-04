## Kata: Reversing Words in a String

# You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here
# are some examples:

# reverse('Hello World') == 'World Hello'
# reverse('Hi There.') == 'There. Hi'

def reverse(st):
	words = st.split(" ")
	words.reverse()
	return (" ").join(words)

if __name__ == "__main__":
	assert reverse('Hello World') == 'World Hello'
	assert reverse('Hi There.') == 'There. Hi'