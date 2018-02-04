## Kata: Good vs Evil

# Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will certainly be involved. Each race has a certain 'worth' when battling against others. On the side of good we have the following races, with their associated worth:

# Hobbits - 1
# Men - 2
# Elves - 3
# Dwarves - 3
# Eagles - 4
# Wizards - 10
# On the side of evil we have:

# Orcs - 1
# Men - 2
# Wargs - 2
# Goblins - 2
# Uruk Hai - 3
# Trolls - 5
# Wizards - 10
# Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

# Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side wins.

# Input:

# The function will be given two parameters. Each parameter will be a string separated by a single space. Each string will contain the count of each race on the side of good and evil.

# The first parameter will contain the count of each race on the side of good in the following order:

# Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
# The second parameter will contain the count of each race on the side of evil in the following order:

# Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
# All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.

# Output:

# Return ""Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.

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