from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

source_code = page.read().decode('utf-8')

#prints index of the <title> tag
print(source_code.find('<title>'))

#finding end of the <title> tag
start_indx_of_title = source_code.find('<title>') + len('<title>')
print(start_indx_of_title)

end_indx_of_title = source_code.find('</title>')
print(end_indx_of_title)

print(source_code[start_indx_of_title:end_indx_of_title])