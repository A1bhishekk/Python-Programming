# get():This method returns the value of the specified keys.
# Syntax:dict.get(key, defaultvalue)

mycar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mycar.get("brand", "BMW"))