import re

print(f'Usage Of re.escape method In Regex Example'.center(100))

in_p = "I went to him at 11 A.M. on 4th July 1886"

# Using \d digit
print('Result OF Escape Pat String  [\d]:', re.escape(in_p))
print('--' * 20)

'''
Output
                             Usage Of re.escape method In Regex Example                             
Result OF Escape Pat String  [\d]: I\ went\ to\ him\ at\ 11\ A\.M\.\ on\ 4th\ July\ 1886
----------------------------------------
'''
