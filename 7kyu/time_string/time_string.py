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




