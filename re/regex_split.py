from re import split

print(f'Usage Of re.Split method In Regex Example'.center(100))

in_p = "I went to him at 11 A.M. on 4th July 1886"
print('Input String:', split('\W+', in_p))
print('--' * 20)

# Using \d digit
print('Input String For [\d]:', split('\d', in_p))
print('--' * 20)

# Using \d+ for numeric values
print('Input String For [\d+]:', split('\d+', in_p))
print('--' * 20)

# Using \D non digit
print('Input String For [\D] :', split('\D', in_p))
print('--' * 20)

# Using \D+ for non  numeric values
print('Input String For [\D+]:', split('\D+', in_p))
print('--' * 20)


# Using \s for single space
print('Input String For [\s]:', split('\s', in_p))
print('--' * 20)

# Using \s+ for multi space
print('Input String For [\s+]:', split('\s+', in_p))
print('--' * 20)

# Using \S for single space
print('Input String For [\S]:', split('\S', in_p))
print('--' * 20)

# Using \S+ for multi space
print('Input String For [\S+]:', split('\S+', in_p))
print('--' * 20)

# Using \S+ for multi space
print('Input String For [\S+]:', split('[h-n]', in_p))
print('--' * 20)

