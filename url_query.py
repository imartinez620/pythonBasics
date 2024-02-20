#https://www.google.com/search?q=cursos+python+development

uri = 'https://www.google.com/search?q='
tags = ['cursos','python','development']
formated_tags = '+'.join(tags)
query_uri = f'{uri}{formated_tags}'

print(query_uri)