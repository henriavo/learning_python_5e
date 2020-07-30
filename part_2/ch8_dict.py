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

# ADDING NEW KEY VALUE ENTRY 🔑 : 💰
mydict['color'] = 'black'
print(mydict)



