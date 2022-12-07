fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
print('Count =',fruits.count('apple'))

print('Index =',fruits.index('banana'))
print('Index =',fruits.index('banana',4)) # finding next banana starting at position 4

# adding to the end of list
fruits.append('grape')
print('After Append =',fruits)

# adding an item at a given position. a.insert([i], 'item')
fruits.insert(4,'Melon') # 4 is the index position 
print('Melon inserted at position 5')
print(fruits)

# reversing the list
fruits.reverse()
print('reversed =',fruits)

# sorting the list - arranges list from a-z order
fruits.sort()
print('sorted =',fruits)

# removing the last item
fruits.pop()
print(fruits)

# removing item in a given position
fruits.pop(4) 
print(fruits)

# we can also use remove() to remove or delete items 
fruits.remove('banana')
print(fruits)
