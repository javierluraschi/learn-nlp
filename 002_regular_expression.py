import re

str = 'user@domain.com'

# extract user from email
pattern = '[a-z]+@[a-z]+\.[a-z]+'
print(re.findall(pattern, str))

# we cal also search and replace with regular expressions
print(re.search(pattern, str))
print(re.sub(pattern, '', str))
