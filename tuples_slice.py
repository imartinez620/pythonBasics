post = ('Python Basiscs', 'Intro Guide to Python', 'Some cool python content','published',
	'other_element')

print(post[:2])
print(post[2:])
print(post[1:3])
print(post[1::2])

#Removing element from end
post = post[:-1]

#Removing element from beginning
post = post[1:]
print(post)

#Removing specific element (messy/not recommended)
post = list(post)
post.remove('Some cool python content')
post = tuple(post)

print(post)

