def fizz_buzz_cuckoo_clock(time):
	time = list(map(int, time.split(":")))
	minute_hand = time[1]
	hour_hand = time[0]
	if time[0] > 12:
		hour_hand = hour_hand - 12
	if time[0] == 0:
		hour_hand = 12
	if minute_hand == 0:
		return " ".join(["Cuckoo"] * hour_hand)
	elif minute_hand == 30:
		return "Cuckoo"
	elif minute_hand % 15 == 0:
		return "Fizz Buzz"
	elif minute_hand % 3 == 0:
		return "Fizz"
	elif minute_hand % 5 == 0:
		return "Buzz"
	else:
		return "tick"

if __name__ == "__main__":
	assert fizz_buzz_cuckoo_clock("13:34") == "tick"
	assert fizz_buzz_cuckoo_clock("21:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"
	assert fizz_buzz_cuckoo_clock("11:15") == "Fizz Buzz"
	assert fizz_buzz_cuckoo_clock("03:03") == "Fizz"
	assert fizz_buzz_cuckoo_clock("14:30") == "Cuckoo"
	assert fizz_buzz_cuckoo_clock("08:55") == "Buzz"
	assert fizz_buzz_cuckoo_clock("00:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"
	assert fizz_buzz_cuckoo_clock("12:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"
