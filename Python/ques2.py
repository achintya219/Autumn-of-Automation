def is_palindrome(n):
	t = n
	r = 0
	while (n > 0):
		d = n%10
		r = r*10 + d
		n = n//10
	if (t==r):
		return True
	else:
		return False

p = int(input())
p += 1

while True:
	if is_palindrome(p) == True:
		break
	else:
		p += 1

print(p)