#!/usr/bin/python3
import copy

print("mutable objects \n")
print("shared references and equality \n")

lista = [23, 41, 66, 11]
listb = lista

if lista == listb:
	print("both lista and listb are variables with same value!\n")

if lista is listb:
	print("both lista and listb are variables pointing to the same object!\n")

listb = copy.copy(lista)

if lista == listb:
	print("STILL same value!\n")

if lista is not listb:
	print("NOT same object!\n")


print("lista is: {}".format(lista))

