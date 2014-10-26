#A variable prefaced by * when calling a function means that the variable contents should be extracted and used as positional arguments. 

def fun1(*args):
	print (args)

def fun2(x, y, *args):
	print (" %s, %s, %s" % (str(x), str(y), str(args)))

fun1(1,2,3)

fun2(1,2,3,45,6,6,7,7,7)
#The same call 
fun2(*[1,2,3,45,6,6,7,7,7])
try:
	#Is not a valid call
	fun2([1,2,3,45,6,6,7,7,7])
except:
	pass


#we introduce ** which does for dictionaries & key/value pairs exactly what * does for iterables and positional parameters. Simple, right?

def fun3(**kwargs):
	print (kwargs)


def fun4(a, b, **kwargs):
	print (a+b)

k = {"a": 1, "b": 2, "c": 3}
fun3(**k)
fun4(**k)



#e neither the name args nor kwargs is part of Python syntax but it is convention to use these variable names when declaring functions


