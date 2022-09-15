def animals(lst):
    print("IFBA",lst,id(lst))
    lst.append("lion")
    print("IFAA",lst,id(lst))

lst=["cow","dog","cat"]
print("BCF",lst,id(lst))
animals(lst)
print("ACF",lst,id(lst))
