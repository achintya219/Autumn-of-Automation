import math

def is_prime(n):
	if n==1:
		return False
	i=2
	while i*i <= n:
		if n%i == 0:
			return False
		i += 1
	return True

d = int(input())
outF = open("myFirstFile.txt", "w")

for val in range(int(math.pow(10, d-1)), int(math.pow(10, d))):
	if val > 1:
		if is_prime(val) == True and val + 2 < int(math.pow(10, d)) and is_prime(val + 2) == True:
			outF.write(str(val))
			outF.write(" ")
			outF.write(str(val+2))
			outF.write("\n")
			val += 2

outF.close()
