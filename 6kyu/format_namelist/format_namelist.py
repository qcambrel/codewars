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