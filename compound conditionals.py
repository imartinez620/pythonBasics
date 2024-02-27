username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow': 
	if password == 'thenorth':
		print('Access permited')
else:
	print('You shall not pass!')

#no es lógico
if username == 'jonsnow' or password == 'thenorth':
    print('Access permited')
else:
	print('You shall not pass!')

#típico
if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
    print('Access permited')
else:
	print('You shall not pass!')

logged_in = True
standard_user = True

#muy usado
if logged_in and not standard_user:
	print('You can access the admin dashboard')
else:
	print('You can only asccess the standard dashboard') 