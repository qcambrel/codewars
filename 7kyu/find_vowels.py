## Kata: Find the vowels

# We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

# So given a string "super", we should return a list of [2, 4].

# Some examples:
# Mmmm  => []
# Super => [2,4]
# Apple => [1,5]
# YoMama -> [1,2,4,6]
# NOTE: Vowels in this context refers to English Language Vowels - a e i o u y

# NOTE: this is indexed from [1..n] (not zero indexed!)

def vowel_indices(word):
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	return [k + 1 for k in range(len(word)) if word[k].lower() in vowels]

if __name__ == "__main__":
	print(vowel_indices("Super"))
	print(vowel_indices("Apple"))
	print(vowel_indices("YoMama"))
	assert vowel_indices("Mmmm") == []
	assert vowel_indices("Super") == [2,4]
	assert vowel_indices("Apple") == [1,5]
	assert vowel_indices("YoMama") == [1,2,4,6]