import re

print(f'Usage Of [ ]  In Regex Example'.center(100))
set_char = re.compile('[a-gA-G]')
print(set_char.findall('Aye, said Mr. Gibenson Stark'))
print('--' * 20)

print(f'Usage Of [\] Char In Regex Example'.center(100))
in_p = "I went to him at 11 A.M. on 4th July 1886"
print('Input String:', in_p)
print('--' * 20)

# Usage of [\d] On Given Input String
pat = re.compile('\d')
print('Return List Of All Single Digit Char:', pat.findall(in_p))
print('-' * 20)

# Usage of [\d+] On Given Input String
pat = re.compile('\d+')
print('Return List Of All Numerical Value:', pat.findall(in_p))
print('-' * 20)

# Usage of [\D] On Given Input String
pat = re.compile('\D')
print('Return List Of All Single Non Numerical Char:', pat.findall(in_p))
print('-' * 20)

# Usage of [\D+] On Given Input String
pat = re.compile('\D+')
print('Return List Of All Non Numerical Words:', pat.findall(in_p))
print('-' * 20)

# Usage Of [\s] Char In Regex Example
pat = re.compile('\s')
print('Return List Of All Space Char:', pat.findall(in_p))
print('-' * 20)

# Usage of [\s+] On Given Input String
pat = re.compile('\s+')
print('Return List Of All Space Word:', pat.findall(in_p))
print('-' * 20)

# Usage of [\S] On Given Input String
pat = re.compile('\S')
print('Return List Of All Single Non Space Char:', pat.findall(in_p))
print('-' * 20)

# Usage of [\S+] On Given Input String
pat = re.compile('\S+')
print('Return List Of All Non Space Words:', pat.findall(in_p))
print('-' * 20)

# Usage Of [\w] Char In Regex Example
pat = re.compile('\w')
print('Return List Of All alphanumeric Char:', pat.findall(in_p))
print('-' * 20)

# Usage of [\w+] On Given Input String
pat = re.compile('\w+')
print('Return List Of All Alphanumeric Word:', pat.findall(in_p))
print('-' * 20)

# Usage of [\W] On Given Input String
pat = re.compile('\W')
print('Return List Of All Single Non Alphanumeric Char:', pat.findall(in_p))
print('-' * 20)

# Usage of [\W+] On Given Input String
pat = re.compile('\W+')
print('Return List Of All Non Alphanumeric Words:', pat.findall(in_p))
print('-' * 20)

print(f'Usage Of [^] Char In Regex Example'.center(100))
in_p = "Went to him at 11 A.M. on 4th July 1886"
print('Input String:', in_p)
print('--' * 20)

pat = re.compile('^W')
print('Starts With:', pat.findall(in_p))
print('-' * 20)

print(f'Usage Of [$] Char In Regex Example'.center(100))
in_p = "ababbaabbbc6"
print('Input String:', in_p)
print('--' * 20)

pat = re.compile('6$')
print('Ends With 6:', pat.findall(in_p))
print('-' * 20)


print(f'Usage Of [*] Char In Regex Example'.center(100))
in_p = "ababbaabbb"
print('Input String:', in_p)
print('--' * 20)

pat = re.compile('ab*')
print('Return List Of All B Occurrence Words:', pat.findall(in_p))
print('-' * 20)

print(f'Usage Of [|] Char In Regex Example'.center(100))
in_p = "ababbaabbbc"
print('Input String:', in_p)
print('--' * 20)

pat = re.compile('a|c')
print('Return List Of All Char Like a\c:', pat.findall(in_p))
print('-' * 20)


