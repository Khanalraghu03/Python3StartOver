# Use bracket instead of curly brackets
foods = ["cheese", "bread", "tomatoes", "rice"]


for i in foods:
    print(i)
    print(len(i))


# # Cannot add/remove from the list w/ tuple
# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)
# print(len(thistuple)

# Can add/remove w/ sets
thisset = set(("apple", "banana", "cherry"))
print(thisset)
thisset.remove("apple")
thisset.add("orange")
print(thisset)


# while looop

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i = i + 1