# List comprehension provides a concise way to create lists.

# creating a list of squares
squares = [] # create an empty array
for x in range(10):
    squares.append(x**2) # adding the squares to the end of list
print(squares)

# we can also create the list this way
ls = list(map(lambda x: x**2, range(10)))
print(ls)

# OR

ls = [x**2 for x in range(10)] # this is more concise and readable
print(ls)

# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
# For example, this listcomp combines the elements of two lists if they are not equal:
comp = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(comp)

# or equivalently
comp = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            comp.append((x,y))
            print(comp)
            
vector = [-4,-2,0,2,4]
print(vector)
# create a new list with the values doubled
new_vector = [x**2 for x in vector]
print(new_vector)
# filter the list to exclude negatives
positives = [x for x in vector if x>=0]
print(positives)
negatives = [x for x in vector if x<0]
print(negatives)

#apply a function to all elements
ls = [abs(x) for x in vector]
print(ls)

# call a method for each element
fruits = ["   banana","  Ovacado","  Lemon","  passion fruit   "]
print(fruits)
fruits = [fruit.strip() for fruit in fruits]
print(fruits)

# create a list of 2-tuples like (number, square)
tuples = [(x, x**2) for x in range(0,10,2)]
# the tuple must be parenthesized (x,x**2), otherwise an error is raised
print(tuples)

# List comprehension can contain complex expressions and nested functions
from math import pi
ls = [str(round(pi, i)) for i in range(1,6)]
print(ls)

# Nested List Comprehension
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

# transpose rows and columns
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)

# or

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) # also make sure to print out of for loop
    
print('New transposed')   
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
    