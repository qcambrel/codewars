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