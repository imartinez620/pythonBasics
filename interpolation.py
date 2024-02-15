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

