import re

print(f'Usage Of re.subn method In Regex Example'.center(100))

in_p = "I went to him at 11 A.M. on 4th July 1886"

# Using \d digit
print('Result OF Sub Pat String  [\d]:', re.subn('\d', 'N', in_p))
print('--' * 20)

# Using \d+ for numeric values
print('Result OF Sub Pat String [\d+]:', re.subn('\d+', 'NN', in_p))
print('--' * 20)

# Using \D non digit
print('Result OF Sub Pat String [\D] :', re.subn('\D+', 'ND', in_p))
print('--' * 20)

# Using \D+ for non  numeric values
print('Result OF Sub Pat String [\D+]:', re.subn('\D+', 'NND', in_p))
print('--' * 20)


# Using \s for single space
print('Result OF Sub Pat String [\s]:', re.subn('\s', 'S', in_p))
print('--' * 20)

# Using \s+ for multi space
print('Result OF Sub Pat String [\s+]:', re.subn('\s+', 'SS', in_p))
print('--' * 20)

# Using \S for single space
print('Result OF Sub Pat String [\S]:', re.subn('\S', 'NS', in_p))
print('--' * 20)

# Using \S+ for multi space
print('Result OF Sub Pat String [\S+]:', re.subn('\S+', 'NSN', in_p))
print('--' * 20)

''' 
OutPut:

Usage Of re.subn method In Regex Example                              
Result OF Sub Pat String  [\d]: ('I went to him at NN A.M. on Nth July NNNN', 7)
----------------------------------------
Result OF Sub Pat String [\d+]: ('I went to him at NN A.M. on NNth July NN', 3)
----------------------------------------
Result OF Sub Pat String [\D] : ('ND11ND4ND1886', 3)
----------------------------------------
Result OF Sub Pat String [\D+]: ('NND11NND4NND1886', 3)
----------------------------------------
Result OF Sub Pat String [\s]: ('ISwentStoShimSatS11SA.M.SonS4thSJulyS1886', 10)
----------------------------------------
Result OF Sub Pat String [\s+]: ('ISSwentSStoSShimSSatSS11SSA.M.SSonSS4thSSJulySS1886', 10)
----------------------------------------
Result OF Sub Pat String [\S]: ('NS NSNSNSNS NSNS NSNSNS NSNS NSNS NSNSNSNS NSNS NSNSNS NSNSNSNS NSNSNSNS', 31)
----------------------------------------
Result OF Sub Pat String [\S+]: ('NSN NSN NSN NSN NSN NSN NSN NSN NSN NSN NSN', 11)
'''