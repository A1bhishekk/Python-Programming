# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# The view object will reflect any changes done to the dictionary, see example below.
# Syntax : dictionary.items()

mycar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

item=mycar.items()
print(item)
print(type(item))

lists=list(item)
print(lists)
print(type(lists))

print(lists[0])
print(lists[0][1])


for r in lists:
    for c in r:
        print(c)
