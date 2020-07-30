#!/usr/bin/python3
import time

print("chapter 8: Lists and Dictionaries\n")

#  :::::::::::::::: LIST COMMON literals AND operations ::::::::::::::

mylist = []
print(f"is mylist empty?: {len(mylist) == 0}\n")
mylist = ["tacos", "sushi", "burgers", "hotdogs"]
print(f"i have {len(mylist)} favorite foods. They are...\n")

for a in mylist:
	print(a,"")
print("\n")

print("...")
time.sleep(1)
print("....\n")

print("New favorite food alert!!! Lets see that list again! ")
mylist.append("indian")
for b in mylist:
	print(b)

print("\n")

query = ""
while query is not "1":
	query = input("Enter a food to search my favorites: ")
	# CHECKING LIST MEMBERSHIP 👇
	print(f"is this food my favorite?: {query in mylist}")
print("\n")
#  ::::: INDEXING AND SLICING :::::::
print(f"the last item in mylist is: {mylist[-1]}")
print(f"the 2 last item in mylist is: {mylist[-2:]}")


#  ::::::::::::::::: USING A LIST LIKE A STACK ::::::::::::::::::
mylist.append("brocoli")
print(mylist)
mylist.pop()
print(mylist)


print("\n")


#  :::::::: OTHER LIST OPERATORS ::::::::::

print(f"index of tacos is: {mylist.index('tacos')}")

mylist.append("brocoli")
mylist.append("ice cream")
print(mylist)
mylist.remove("brocoli")
print(mylist)






