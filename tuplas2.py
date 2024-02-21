post = ('Python Basiscs', 'Intro Guide to Python', 'Some cool python content')

print(id(post))

post = post + ('published',) #put ','

print(id(post))

title, sub_heading, content, status = post
print(title)
print(sub_heading)
print(content)
print(status)

