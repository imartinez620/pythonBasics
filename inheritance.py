class User:
	def __init__(self, email, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def greeting(self):
		return(f'Hi {self.first_name} {self.last_name}')

class AdminUser(User):
	def active_users(self):
		return '500'

peter = AdminUser('peter@parker.es', 'Peter', 'Parker')
bruce = User('bruce@wayne.es', 'Bruce', 'Wayne')

print(peter.active_users())
print(peter.greeting())