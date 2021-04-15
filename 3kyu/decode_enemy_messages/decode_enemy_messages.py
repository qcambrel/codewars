import string
import math

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = "!@#$%^&*()_+-"
punctuation = [item for item in string.punctation if item not in special_characters]
punctation = "".join(punctuation)

encodables = lowercase + uppercase + digits + punctuation + " " 

def encode2(msg):
	encoded_msg = ''
	for k in range(msg):
		char = msg[k]
		if char in encodables:
			base_value = encodables.index(char) + 1
			current_value = base_value * 2**k
			temp_encodables = [encodables] * math.ceil(current_value / (len(encodables)))
			temp_encodables = "".join(temp_encodables)
			encoded_msg += temp_encodables[current_value - 1]
		else:
			encoded_msg += char
	return encoded_msg


