# ## Kata: 1RM Calculator

# You just got done with your set at the gym, and you are wondering how much weight you could lift if you did a single repetition. Thankfully, a few scholars have devised formulas for this purpose (from Wikipedia) :

# Epley
# 1 RM=w(1+r30)\Large\text{1 RM} = w(1 + \frac{r}{30})1 RM=w(1+ 
# 30
# r
# ​	
#  )
# McGlothin
# 1 RM=100w101.3−2.67123r\Large\text{1 RM} = \frac{100w}{101.3 - 2.67123r}1 RM= 
# 101.3−2.67123r
# 100w
# ​	
 
# Lombardi
# 1 RM=wr0.10\Large\text{1 RM} = wr^{0.10}1 RM=wr 
# 0.10
 
# Your function will receive a weight w and a number of repetitions r and must return your projected one repetition maximum. Since you are not sure which formula to use and you are feeling confident, your function will return the largest value from the three formulas shown above, rounded to the nearest integer. However, if the number of repetitions passed in is 1 (i.e., it is already a one rep max), your function must return w. Also, if the number of repetitions passed in is 0 (i.e., no repetitions were completed), your function must return 0.

def calculate_1RM(weight, reps):
	if reps in [0, 1]:
		return reps * weight
	epley_max = weight * (1 + reps / 30)
	mcglothin_max = (100 * weight) / (101.3 - 2.67123 * reps)
	lombardi_max = weight * reps ** 0.10
	return round(max([epley_max, mcglothin_max, lombardi_max]))


assert calculate_1RM(135,20) == 282
assert calculate_1RM(200,8) == 253
assert calculate_1RM(270,2) == 289
assert calculate_1RM(360,1) == 360
assert calculate_1RM(400,0) == 0