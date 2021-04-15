def cakes(recipe, available):
	for ingredient in recipe.keys():
		if ingredient not in available.keys():
			return 0
	possible_cakes = sorted([available[ingredient] // recipe[ingredient] for ingredient in recipe.keys()])
	return possible_cakes[0]

if __name__ == "__main__":
	assert cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2
	assert cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}) == 0