#!/usr/bin/python3

# ::::::::: CHAPTER 8. DICTIONARIES. :::::::::::::
mydict = {'type': 'mobile', 'manufacturer':'apple', 'storage':'128'}

# ACCES VALUES USING LITERAL 👇
print(f"My device type is: {mydict['type']}")

#  ACCESING VALUES USING METHOD 👇
print(f"My device manufacturer is: {mydict.get('manufacturer') } ")
print(f"My device storage size is: {mydict.get('storage') } ")

#  ATTEMPT TO GET KEY THAT DOES NOT EXISTS, SET A DEFAULT
print(f"My device screen size is: {mydict.get('screen size', '4.7') } ")

# ADDING NEW KEY VALUE ENTRY (MUTABLE ACTION)
mydict['color'] = 'black'
print(mydict)

# CHECK IF A KEY EXISTS 👇
result = 'purchase_date' in mydict
print(f"does the key 'purchase_date' exist?: {result}")

result = 'manufacturer' in mydict
print(f"does the key 'manufacturer' exist?: {result}")


# DELETE AN ENTRY (MUTABLE ACTION) 👇
del mydict['color']
print(mydict, "\n")


# LOOP ON A DICTIONARY. NO EXPECTED ORDERING. 
for key in mydict:
	print(f"key: {key} value: {mydict[key]}")




# :::: CHAPTER 8: QUIZ :::::::::

#  2 WAYS TO BUILD A LIST WITH FIVE INTEGER ZEROS:
daList = [0]*5
print(daList)

daList2 =[0,0,0,0,0,]
print(daList2)

#  2 WAY TO BUILD A DICTIONARY WITH TWO KEYS'a' 'b' WITH VALUE '0'
mappingOne = {'a':0, 'b':0}
print(mappingOne)
mappingTwo = dict(a=0, b=0)
print(mappingTwo)

listOne = [6,7,8,9,10]

listOne.append(11)
print(listOne)

listOne.pop()
print(listOne)

del listOne[0]
print(listOne)

listOne.remove(8)
print(listOne)

#  FOUR OPERATIONS TO CHANGE DICTIONARY IN PLACE
print("\n")
mappingOne['c'] = 99
print(mappingOne)

del mappingOne['c'] 
print(mappingOne)

mappingOne['a'] = 44
print(mappingOne)

mappingOne['a'] = [0,44]
print(mappingOne, "\n")

# ::::::::: ACCESS ALL KEYS. ACCESS ALL VALUES. AS KEYS AND TUPLES ::::::
r1 = mappingOne.values()
print(list(r1))
print(tuple(r1))

r2 = mappingOne.keys()
print(list(r2))
print(tuple(r2))

r3 = mappingOne.items()
print(list(r3))










