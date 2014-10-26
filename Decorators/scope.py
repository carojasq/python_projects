a = "Global variable"

# Function parameters can have names or positions
def foo(a, y=0):
	a = "Cadena local"
	print (a) # First loooks on locals variables, then  in global
	# global a # Overwriting global variable
	print (locals())
	print (globals())

#gl = globals()
#print (gl['__file__'])
#print (globals())
foo(a)
print (a)