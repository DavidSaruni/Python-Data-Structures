# PYTHON DICTIONARIES

tel = {'jack':4040, 'ma':4041}
print(tel)
tel['zuckerburg'] = 4042
print(tel)

del tel['ma']
print(tel)
tel['captain'] = 4039
print(tel)
print(list(tel))
print(sorted(tel))
print('captain' in tel)
print('jack' not in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
d=dict([('Captain', 200), ('Justine', 250), ('Nicolas', 300)])
print(d)

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
squares = {x:x**2 for x in (2,4,6,8,10)}
print(squares)

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
names = dict(james = 6000, david = 6500, justine = 7000)
print(names)

# LOOPING TECHNIQUES
# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['ding', 'dong', 'dung']):
    print(i,v)
    
# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['Captain', 'the night school movie', 'maroon']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1,10,2)):
    print(i)
    
# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# removing duplicates using set(). 
# The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):
    print(fruit)
    
# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
