# class Html:
# 	def __init__(self, content):
# 		self.content = content

# 	def render(self):
# 		raise NotImplementedError('Subclass must implement render method')

# class Heading(Html):
# 	def render(self):
# 		return f'<h1>{self.content}</h1>'

# class Div(Html):
# 	def render(self):
# 		return f'<div>{self.content}</div>'

# tags = [
# 		Div('Some content'),
# 		Heading('Some big heading'),
# 		Div('Another div')
# 		]

# for tag in tags:
# 	print(tag.render())


class Heading:
	def __init__(self, content):
		self.content = content

	def render(self):
		return f'<h1>{self.content}</h1>'

class Div:
	def __init__(self, content):
		self.content = content

	def render(self):
		return f'<div>{self.content}</div>'


div_one = Div('Some content')
heading = Heading('Some big heading')
div_two = Div('Another div')

def html_render(tag_object):
	print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)