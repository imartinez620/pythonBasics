#List: []
#Dictionary: {}
#Tuple: ()

post = ('Python Basiscs', 'Intro Guide to Python', 'Some cool python content')

title, sub_heading, content = post

"""
title = post[0]
sub_heading = post[1]
content = post[2]
"""
print(title)
print(sub_heading)
print(content)


#tuple is immutable
#list is mutable

list_post = ['Python Basiscs', 'Intro Guide to Python', 'Some cool python content']
list_post.sort() #alteras la lista

title, sub_heading, content = list_post
print(title)
print(sub_heading)
print(content)
