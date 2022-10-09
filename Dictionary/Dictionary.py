# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

mycar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mycar)
print(id(mycar))

# Accesing item  
print(mycar["brand"])


# Modifying 
mycar["model"] = "Mustang GT"
print(f"After modifying : {mycar}, {id(mycar)}")

# Inserting
mycar["Price"]=10000000
print(f"After inserting : {mycar}, {id(mycar)}")


# Deletion 
# Deleting an element
del mycar["brand"]
print(f"After deletting : {mycar}, {id(mycar)}")

# Deleting entire dictionary
del mycar
print(f"After deleting : {mycar}")


