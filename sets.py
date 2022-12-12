# Python sets
# A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. 
# # Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

basket = {'apple', 'orange', 'apple', 'pear', 'banana'}
print(basket) # shows duplicates have been removed
print('orange' in basket) # fast membership testing
print('crabgrass' in basket)

# demonstrating different set operations

a = set('abracadabra')
b = set('alacazam')
print(a) # shows unique letters in a
print(a-b) # letters in a but not in b
print(a | b) # letters in a or b or both
print(a&b) # letters in both a and b
print(a^b) # letters in a or b but not both

# SET COMPREHENSION
c = {x for x in 'abracadabra' if x not in 'abd'}
print(c)
