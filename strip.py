url = '   https://www.google.es   '

print(url.strip())
print(url.strip().lstrip('https://'))


url = '  https://www.google.es   '
url = url.strip()
url = url.lstrip('htps:/w.')
url = url.rstrip('es')
url = url.rstrip('.')
url = url.capitalize()

print(url)