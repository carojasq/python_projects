def outer(x):
	print ("Outer")
	def inner():
		print ("Inside inner %s" % (str(x)))
	return inner

inner_function = outer(1)
print ("Executing inner")
inner_function()