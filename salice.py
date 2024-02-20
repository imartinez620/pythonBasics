tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

print(tags[1:4:2])

slice_obj = slice(1,4,2)
print(slice_obj)

print(tags[slice_obj])
print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

tags.extend(['GYM'])

print(tags)

new_tags = tags + ['Cocina']
print(new_tags)