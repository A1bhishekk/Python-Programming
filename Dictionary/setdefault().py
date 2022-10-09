# Definition and Usage
# The setdefault() method returns the value of the item with the specified key.

# If the key does not exist, insert the key, with the specified value, see example below

# Syntax : dictionary.setdefault(keyname, value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("price", "1000000000")
print(car)
print(x)