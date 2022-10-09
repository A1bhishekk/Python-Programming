# Definition and Usage
# The update() method inserts the specified items to the dictionary.

# The specified items can be a dictionary, or an iterable object with key value pairs.

# Syntax : dictionary.update(iterable)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(f"Before Update:{car} ,{id(car)}")
values={"color": "black","price":100000000}
# car.update({"color": "yellow"})
car.update(values)

print(f"After update:{car} ,{id(car)}")