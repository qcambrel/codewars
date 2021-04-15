def is_mininimum_length(number):
	return len(number) >= 3

def is_round(number):
	return set(number[1:]) == {'0'}

def is_repdigit(number):
	return len(set(number)) == 1

def is_increasing_sequence(number):
	return number in ''.join([str(n) if n < 10 else '0' for n in range(1, 11)])

def is_decreasing_sequence(number):
	return number in ''.join([str(n) for n in range(9, -1, -1)])

def is_palindrome(number):
	return list(reversed(list(number))) == list(number)

def evaluate(number, awesome_phrases):
	number = str(number)
	constraints = (
		is_round(number) and is_mininimum_length(number),
		is_repdigit(number) and is_mininimum_length(number),
		is_increasing_sequence(number) and is_mininimum_length(number),
		is_decreasing_sequence(number) and is_mininimum_length(number),
		is_palindrome(number) and is_mininimum_length(number),
		int(number) in awesome_phrases and is_mininimum_length(number)
	)
	return constraints
	
def is_interesting(number, awesome_phrases):
	evaluation = {
		True not in evaluate(number, awesome_phrases):0,
		True in evaluate(number + 2, awesome_phrases):1,
		True in evaluate(number + 1, awesome_phrases):1,
		True in evaluate(number, awesome_phrases):2
	}
	return evaluation[True]