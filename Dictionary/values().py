# Definition and Usage
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# The view object will reflect any changes done to the dictionary, see example below.
# Syntax : dictionary.values()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)