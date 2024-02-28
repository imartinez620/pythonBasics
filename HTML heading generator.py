"""
heading_generator(title, heading_type)

heading_generator('Greeting', '1')
<h1>Greeting</h1>
heading_generator('Hi there', '3')
<h3>Hi there</h3>
"""

def heading_generator(title, heading_type):
	print(f"<h{heading_type}>{title}</h{heading_type}>")

heading_generator('Greeting', '1')
heading_generator('Hi there', '3')

#solution
def heading_generator(title, heading_type):
	return("<h{0}>".format(heading_type) +f"{title}" + 
		"</h{0}>".format(heading_type))

