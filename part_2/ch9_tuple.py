import sys
# :::::::::::; CHAPTER 9. TUPLES ::::::::::::

# CONCATINATION
t1 = (3,4,5)

t2 = (6,7,8)

print(t1)
print(t2)
r = t1 + t2
print(r)
# ::::::::::::: REPITITION ::::::::::::::::

t9 = t1*3
print(t9)
print("\n")


# :::::::::::::: LIST <-> TUPLE CONVERSIONS ::::::::::::

l1 = ["new york", "chicago", "houston"]
print(type(l1))
print(l1)
#  SORT A TYPLE WITH BUILT IN
#  NEED TO ASSIGN TO NEW VARIABLE SINCE TUPLE ARE IMMUTABLE
ls = sorted(l1)
print(ls)

t1 = tuple(l1)
print(type(t1))
print(t1)

t9 = t1 + ("atlanta", "miami")
print(type(t9))
print(t9)

l9 = list(t9)
print(type(l9))
print(l9)
#  SORT A LIST
l9.sort()
print(l9)
print("\n")

# :::::::::::::::::	ACCESSING :::::::

print("I live in the city of: ", str(t9[1]) )
print("Or I can live in these two cities as well:", str(t9[4]), "or", str(t9[0]))
print("Or I can live in these two cities as well:", t9[2:])

# SINGLE ITEM TUPLE
cr = 42,
print(type(cr))
print(cr)
print("************\n")

# USING TYPLES AS DICTIONARY KEYS
d1 = {11:"hardway", 77:"Luka", (24,8):"bryant"}
print(d1)


#  SKIPPED FILES

