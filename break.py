usernames = [
	'jon',
	'tyrion',
	'theon',
	'cersey',
	'sansa'
]

#Continue
for username in usernames:
	if username == 'cersey':
		print(f'Sorry, {username}, you are not allowed.')
		continue
	else:
		print(f'{username} is allowed.')

#Break
for username in usernames:
	if username == 'cersey':
		print(f'{username} was found at index {username.index(username)}')
		break
	print(username)