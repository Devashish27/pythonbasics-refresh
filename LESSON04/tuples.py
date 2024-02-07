# Tuples....
mytuple = tuple(('tyron', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Tyron')
newtuple = tuple(newlist)
print(newtuple)

# Unpacking tuples..
# (one, two, *hey) = anothertuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
# print(anothertuple)

print(anothertuple.count(2))
