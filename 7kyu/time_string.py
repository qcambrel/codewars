## Kata: Correct the time-string

# A new task for you!

# You have to create a method, that corrects a given time string. There was a problem in addition, so many of the time strings are broken. Time-Format is european. So from "00:00:00" to "23:59:59". 

# Some examples:

# "09:10:01" -> "09:10:01"
# "11:70:10" -> "12:10:10"
# "19:99:99" -> "20:40:39"
# "24:01:01" -> "00:01:01"

# If the input-string is null or empty return exactly this value! (empty string for C++)
# If the time-string-format is invalid, return null. (empty string for C++)

# Have fun coding it and please don't forget to vote and rank this kata! :-)

# I have created other katas. Have a look if you like coding and challenges.

def time_correct(t):
	if t:
		try:
			standard = {'hours': 24, 'minutes': 60, 'seconds': 60}
			units = list(standard.keys())
			t = list(map(int, t.split(":")))
			if t[1] > 59:
				t[1] = t[1] % standard[units[1]]
				t[0] = t[0] + t[1] // standard[units[1]]
			if t[2] > 59:
				t[2] = t[2] % standard[units[2]]
				t[1] = t[1] + t[2] // standard[units[2]]
				if t[1] > 59:
					t[1] = t[1] % standard[units[1]]
					t[0] = t[0] + t[1] // standard[units[1]]
			t = ":".join(["0" + str(i) if i < 10 else str(i) for i in t])
		except ValueError:
			t = None
		except IndexError:
			t = None
	return t




