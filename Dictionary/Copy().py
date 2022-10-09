
mycar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(f"Before copy :{mycar},{id(mycar)}")
# new_car = mycar
new_car=mycar.copy()
print(f"After copy:{new_car} ,{id(new_car)}")