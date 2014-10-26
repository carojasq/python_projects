def logger(func):
	def inner(*args, **kwargs):
		print ("Here are the args %s \n The kwargs %s \nthe function name is: %s \ndecorator name: %s" % (str(args), str(kwargs), func.__name__, __name__))
		return func(*args, **kwargs)
	return inner

@logger
def sum(a,b):
	return (a+b)

print (sum(1,2))
