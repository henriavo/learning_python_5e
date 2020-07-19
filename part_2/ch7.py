#!/usr/bin/python3

print("Python String Fundamentals \n")


# :::::::::::: String formatting ::::::::::::
name = "henri W idrovo"

print(f"My name is: {name}")

name = name.replace("W", "William")

print(f"My name is: {name}")

print(f"My middle name is: {name[6:13]}")

print(f"My middle name is: {name.split(' ')[1]}")

# :::::::::::: triple quotes ::::::::::::

bio = '''
Hello world,
My favorite food is tacos,
and my favorite color is orange
'''

print(bio)

# :::::::::::: string repitiion 🔁::::::::::::
print(":" * 50)

# :::::::::::: string slicing! 🔪 ::::::::::::

nums = "0123456789"

print(f"slice 0-4: {nums[:5]}")
print(f"slice 4-7: {nums[4:8]}")
print(f"slice 7-9: {nums[7:]}")
print(f"slice everything. copy! : {nums[:]}")

# :::::::::::: str <-> int and float (conversion tools) 🚜::::::::::::
anInt = 433
aStr = "688"

print(f"anInt type: {type(anInt)}")
anInt = str(anInt)
print(f"anInt type: {type(anInt)}]\n")

print(f"aStr type: {type(aStr)}")
aStr = int(aStr)
print(f"aStr type: {type(aStr)}\n")

aFloat = 11.3444
print(f"aFloat type: {type(aFloat)}")
aFloat = str(aFloat)
print(f"aFloat type: {type(aFloat)}")
aFloat = float(aFloat)
print(f"aFloat type: {type(aFloat)}\n")


# :::::::::::: to change a string, make a new one 🆕 :::::::::::::

path = "path/to/porn"
print(path + '\n')
print(f"do i need to change this path?: {path.endswith('porn')}\n")

path = path[:8] + "homework"
print(path + "\n")

# :::::::::::::::: some String methods :::::::::::::::::::::

address = "123 fake st"
address = address.replace(" ", "")
print(f"address is alpha numeric? : {address.isalnum()}")

number = "39847658937"
print(f"number is numeric? : {number.isnumeric()}")

letters = "afoijusdfihnoiehjs"
print(f"letters is upper? : {letters.isupper()}")
letters = letters.upper()
print(f"letters is upper? : {letters.isupper()}")






