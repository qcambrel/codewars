## Kata: Format a string of names like 'Bart, Lisa & Maggie'

# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except
# for the last two names, which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
	if len(names) > 1:
		return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
								names[-1]['name'])
	elif names:
		return names[0]['name']
	else:
		return ''

if __name__ == "__main__":
	assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge'
	assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]) == 'Bart, Lisa & Maggie'
	assert namelist([{'name': 'Bart'},{'name': 'Lisa'}]) == 'Bart & Lisa'
	assert namelist([{'name': 'Bart'}]) == 'Bart'
	assert namelist([]) == ''