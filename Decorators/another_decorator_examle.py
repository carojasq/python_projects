class Coordinate(object): #  Inherits from the same class as all the python objects

	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def __repr__ (self): # String representation
		return "Coordinates are %s" % (self.__dict__)

def add(a,b):
	return Coordinate(a.x + b.x, a.y + b.y)

def sus(a,b):
	return Coordinate(a.x - b.x, a.y - b.y)


def wrapper(func):
	def checker(a,b):
		if a.x <0 or a.y<0:
			a = Coordinate(a.x if a.x>0 else 0, a.y if a.y>0 else 0)
		if b.x <0 or b.y<0:
			b = Coordinate(b.x if b.x>0 else 0, b.y if b.y>0 else 0)
		ret = func(a,b)
		if ret.x <0 or ret.y<0:
			ret = Coordinate(ret.x if ret.x>0 else 0, ret.y if ret.y>0 else 0)
		return ret
	return checker

c1 = Coordinate(10,10)
c1n = Coordinate(9,11)
c1ln = Coordinate(11,11)
c2 = Coordinate(1,1)
print ("Before decoration")
print (add(c1, c2))
print (sus(c1, c2))
print ("After decoration")
sus = wrapper(sus)
print (sus(c1, c1n))
print (sus(c1, c1ln))



#We can decorate our function using @ before definition
@wrapper 
def sus(a,b):
	return Coordinate(a.x - b.x, a.y - b.y)



