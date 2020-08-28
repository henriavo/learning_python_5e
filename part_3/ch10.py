
while True:
	reply = input("enter something:")
	if reply == "stop": break
	print(reply.upper())

while True:
	reply = input("enter a number:")
	if reply == "stop": break
	replyInt = int(reply)
	print(replyInt ** 2)

while True:
	x = input("enter anything!")
	if x == "stop": break
	elif not x.isdigit(): print("BAD! " * 3)
	else: print(int(x) * 2)


while True:
	x = input("enter something:")
	if x == "stop": break
	try:
		num = int(x)
	except:
		print("BAD! " * 3)
	else:
		print(num * 2)
