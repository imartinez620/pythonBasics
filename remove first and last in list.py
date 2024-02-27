"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'some content', '</h1>']

remove_first_and_last(html)
=> ['some content']

html_2 = ['<h1>', 'some content', 'more', '</h1>']
remove_first_and_last(html_2)
=> ['some content', 'more']

one, *two, three = [1,2,3,4]
"""

def remove_first_and_last(list_to_clean):
	list_shorted = list_to_clean[1:]
	last_element = list_shorted.pop()
	return list_shorted


html = ['<h1>', 'some content', '</h1>']
print(remove_first_and_last(html))

html_2 = ['<h1>', 'some content', 'more', '</h1>']
print(remove_first_and_last(html_2))

#solution
def remove_first_and_last(list_to_clean):
	_, *list_shorted, _ = list_to_clean #'* almacena todo lo del medio'
	return list_shorted


html = ['<h1>', 'some content', '</h1>']
print(remove_first_and_last(html))

html_2 = ['<h1>', 'some content', 'more', '</h1>']
print(remove_first_and_last(html_2))