# Definition and Usage
# The pop() method removes the specified item from the dictionary.

# The value of the removed item is the return value of the pop() method, see example below.

# Syntax : dictionary.pop(keyname, defaultvalue)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("models","bmw")

print(car)