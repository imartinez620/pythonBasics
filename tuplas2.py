post = ('Python Basiscs', 'Intro Guide to Python', 'Some cool python content')

print(id(post))

post = post + ('published',) #put ','

print(id(post))

title, sub_heading, content, status = post
print(title)
print(sub_heading)
print(content)
print(status)

post += (['tag1','tag2'],)

_,_,_,_,tags = post
print(tags) 

#Solution
tags_b = ['python','coding','tutorial']
post += (tags_b,)

print(post[-1][1])

