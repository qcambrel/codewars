## Kata: Convert string to camel case

# Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. The first word within the output
# should be capitalized only if the original word was capitalized.

# Examples:

# returns "theStealthWarrior"
# to_camel_case("the-stealth-warrior") 

# returns "TheStealthWarrior"
# to_camel_case("The_Stealth_Warrior")

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