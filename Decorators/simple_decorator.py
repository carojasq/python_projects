#A decorator is just a callable that takes a function as an argument and returns a replacement function. 

def outer(func):
	def inner():
		f = func()
		return f+1
	return inner

def func1():
	return 1

decorated  = outer(func1) # Decorated is a decorated version of func1
func1  = outer(func1) #Func1 reassigned
print (decorated())
print (func1())
