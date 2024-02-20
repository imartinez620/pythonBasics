tags = ['python','development','tutorials','code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

#sort_list
print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

#Ranges
tag_range = tags[0:3]
print(f'Rango {tag_range}')
