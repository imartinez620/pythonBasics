tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

#tag_range = tags[:-1:2]
tag_range = tags[::-1]
tags.sort(reverse=True)

print(tag_range)
print(tags)

tags_sorted_error = tags.sort()
print(tags_sorted_error)


