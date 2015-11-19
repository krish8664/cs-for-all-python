
class Rational:
    ''' A rational object with numerator or denominator '''
    def __init__(self, num, denom):
	self.numerator = num
	self.denominator = denom
    ''' A function to add two rational numbers'''
    def add(self, other):
	newNumerator = self.numerator * other.denominator + other.numerator * self.denominator
	newDenominator = self.denominator * other.denominator
	return Rational(newNumerator, newDenominator)
    ''' A function to compare two rational numbers, overloaded with >= operator'''
    def __ge__(self, other):
	return self.numerator * other.denominator >= self.denominator * other.numerator

r1 = Rational(10,20) #create a rational number 10/20
r2 = Rational(20, 10) #create a ration numner 20/10
print r1 
print r1.numerator
print r1.denominator
print r1.add(r2).numerator #print r1 + r2, not overloaded
print r2 >= r1 #print if r2 > r1, function ge is overloaded with >= 
