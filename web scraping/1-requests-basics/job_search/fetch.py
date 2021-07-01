from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

source_code = page.read().decode('utf-8')

#prints index of the <title> tag
print(source_code.find('<title>'))

#<title> </title>

print()
