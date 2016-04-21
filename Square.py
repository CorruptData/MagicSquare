def magic(size, power):
	numbox = initval = size ** 2
	a = [1] * numbox
	maxsize = 10
	for i in range(0,numbox):
		a[i] = initval
		initval -= 1
		print a[i]
	
	a[0] -= 1
	while (a[numbox-1] < maxsize):
		a[0] += 1
		a = rollover(a, numbox, maxsize)
		if (checkdubs(a, numbox)):
			continue
		addemup(a, size, power, numbox)
		
	return "END"

def rollover(a, numbox, maxsize):
	for l in range(0,numbox):
		if (a[l] > maxsize):
			a[l] = 1
			a[l+1] += 1
	return a

def checkdubs(a, numbox):
	for j in range(0,numbox):
		for k in range(0,numbox):
			if ((a[j] == a[k]) and not (j == k)):
				return True

def addemup(a, size, power, numbox):
	f = [0] * ((size * 2) + 2)
	across = 0
	down = 0
	diagup = 0
	diagdown = 0
	for m in range(0, size):
		for n in range(0, size):
			across += a[m+n] ** power
			down += a[m+(n*size)] ** power
		diagup += a[(m*size)+(size-m-1)]
		diagdown += a[(m*size)+m]
		f[m] = across
		f[m+size] = down
	
	f[2*size] = diagup
	f[(2*size)+1] = diagdown

print(magic(3, 1))
