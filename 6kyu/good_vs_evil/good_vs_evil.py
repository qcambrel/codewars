def goodVsEvil(good, evil):
	print good
	print evil
	outcomes = {True: "Battle Result: Good triumphs over Evil",
	 			False: "Battle Result: Evil eradicates all trace of Good"}
	good_races = [("hobbits", 1), ("men", 2), ("elves", 3),
				  ("dwarves", 3), ("eagles", 4), ("wizards", 10)]
	evil_races = [("orcs", 1), ("men", 2), ("wargs", 2), ("goblins", 2), 
				  ("uruk hai", 3), ("trolls", 5), ("wizards", 10)]
	forces_of_good = list(map(int, good.split(" ")))
	forces_of_evil = list(map(int, evil.split(" ")))
	strength_of_good = 0
	strength_of_evil = 0
	for k in range(len(forces_of_good)):
		race = good_races[k][1]
		number = forces_of_good[k]
		strength_of_good = strength_of_good + (race * number)
	print strength_of_good
	for k in range(len(forces_of_evil)):
		race = evil_races[k][1]
		number = forces_of_evil[k]
		strength_of_evil = strength_of_evil + (race * number)
	print strength_of_evil
	if strength_of_good == strength_of_evil:
		return "Battle Result: No victor on this battle field"
	return outcomes[strength_of_good > strength_of_evil]