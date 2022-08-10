import re

str = '123123adsfbdsf bc aaaaaaaaaaaaaaabc5 xbc fbc sdsff 3sdfsdf'

# extract user from email

# print(re.sub('abc', '', str))
# print(re.search('abc', str))

print(re.findall('[af]+bc.', str))

# jluraschi
