def logger(func):
	def inner(*args, **kwargs):
		print ("Here are the args %s \n and the kwargs %s, function name is %s" % (str(args), str(kwargs), func.__name__))
		return func(*args, **kwargs)
	return inner

@logger
def sum(a,b):
	return a+b

print sum(1,2)