file = open('num.txt' , "r")
x = file.readline()

while file:
	x = x.strip().split(",")#making a list
	l = len(x)

	#converting to integer
	for m in range(l):
		x[m] = int(x[m])

	print("The unsorted list is ", x)

	#bubble sorting
	for y in range(l):
		for z in range(l-y-1):
			if x[z]>x[z+1]:
				x[z],x[z+1] = x[z+1],x[z]

	break
	x = file.readline()

print("List after sorted >> ",x)
file.close()
