# python tuple is a collection of objects separated by commas.
var = ('Come', 'and', 'study', 'python')
print(var)

# Accessing values in the tuples
print('Value of var[0] =',var[0])
print('Value of var[1] =',var[1])

# Concatenating Python tuples
tuple1 = (0,1,2,3)
tuple2 = ('Python', 'Django', 'React', 'HTML')
tuple3 = (tuple1+tuple2)
print(tuple3)

# Nesting of Python Tuples
tuple4 = (tuple1, tuple2)
print(tuple4)

# Repetition of Tuples
tuple = ('captain',)*3 # try without comma - (captaincaptaincaptain)
print(tuple)

# tuples are immutable - meaning we can not change values in a tuple once they are created
digits = (0,1,2,3,4,5)
# digits[0] = 4
# print(digits) # it will raise an error

# slicing a tuple
digits = (0,1,2,3,4,5)
print(digits[1:]) # displaying from index 1
print(digits[::-1]) # reversing the tuple
print(digits[2:5]) # displaying a given range

# finding length of a tuple
print(len(digits))

# tuple looping and unpacking
for i in digits:
    print(i)

# # unpacking tuple
# for a,b,c,d,e in digits:
#     print(a,b,c,d,e)