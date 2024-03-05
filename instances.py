class Website:
	def __init__(self, title, size):
		self.title = title
		self.size = size

my_web = Website("My Website", 500)
print(my_web.title)
print(my_web.__dict__)

my_web_two = Website("My Second Website", 100)
print(my_web_two.title)
print(my_web_two.__dict__)

class DifferentWebsite:
	title = "My Different Website"

my_web_three = DifferentWebsite()
print(my_web_three.title)

