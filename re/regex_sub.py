import re

print(f'Usage Of re.sub method In Regex Example'.center(100))

in_p = "I went to him at 11 A.M. on 4th July 1886"

# Using \d digit
print('Result OF Sub Pat String  [\d]:', re.sub('\d', 'N', in_p))
print('--' * 20)

# Using \d+ for numeric values
print('Result OF Sub Pat String [\d+]:', re.sub('\d+', 'NN', in_p))
print('--' * 20)

# Using \D non digit
print('Result OF Sub Pat String [\D] :', re.sub('\D+', 'ND', in_p))
print('--' * 20)

# Using \D+ for non  numeric values
print('Result OF Sub Pat String [\D+]:', re.sub('\D+', 'NND', in_p))
print('--' * 20)


# Using \s for single space
print('Result OF Sub Pat String [\s]:', re.sub('\s', 'S', in_p))
print('--' * 20)

# Using \s+ for multi space
print('Result OF Sub Pat String [\s+]:', re.sub('\s+', 'SS', in_p))
print('--' * 20)

# Using \S for single space
print('Result OF Sub Pat String [\S]:', re.sub('\S', 'NS', in_p))
print('--' * 20)

# Using \S+ for multi space
print('Result OF Sub Pat String [\S+]:', re.sub('\S+', 'NSN', in_p))
print('--' * 20)

