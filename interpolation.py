name = 'Kristine'
product = "Course of Python"
greeting = f'Hi {name}'

print(greeting)

greeting = f'Hi {2+2}'
print(greeting)

greeting = f'Hi {{2+2}}'
print(greeting)

greeting = f"""
Dear {name},

Thank you for select our {product}.

Regards,
Me
"""

print(greeting)

greeting = "Hi {0}, thank you for learning this {1}.".format(name, product)

print(greeting)
print("The sum of 1 + 2 is {0}".format(1+2))


