#regular expressions are patterns that can be used to search for a text within a string

import re

#finds fs in wesfsdf 
print(re.findall('fs', 'wesfsdf'))

#finds for begins with a and end with c
print(re.findall('ab*c','abcd'))

print(re.findall('ab*c','acc'))

#ignores case sensivity
print(re.findall("ab*c", "ABC", re.IGNORECASE))

# .* states any number of characters can contains between a and c
print(re.findall("a.*c", "abc"))



