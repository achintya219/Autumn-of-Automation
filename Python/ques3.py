import math

class Complex(object):
	def __init__(self, real, imag=0.0):
		self.real = real
		self.imag = imag

	def add(self, other):
		return Complex(self.real + other.real, self.imag + other.imag)

	def sub(self, other):
		return Complex(self.real - other.real, self.imag - other.imag)

	def mul(self, other):
		return Complex(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)

	def magnitude(self):
		return math.sqrt(self.real*self.real + self.imag*self.imag)

	def conjugate(self):
		return Complex(self.real, -self.imag)

	def display(self):
		if self.imag >= 0:
			print(self.real,"+",self.imag,"i\n")
		else:
			print(self.real,self.imag,"i\n")

a = Complex(1,2)
a.display()
a.conjugate().display()
b = Complex(2, -3)
b.display()
c = b.add(a)
c.display()
d = b.mul(a)
d.display()