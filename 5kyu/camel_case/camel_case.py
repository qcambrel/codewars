def to_camel_case(text):
	words = text.replace("-", "_").split("_")
	for k in range(len(words)):
		if k > 0:
			words[k] = words[k].replace(words[k][0], words[k][0].upper(), 1)
	return ("").join(words)

if __name__ == "__main__":
	assert to_camel_case("") == ""
	assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
	assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
	assert to_camel_case("A-B-C") == "ABC"