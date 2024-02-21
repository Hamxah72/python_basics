def make_counter():
	count = 0 
	def counter():
		nonlocal count # Using nonlocal to modify the count variable 
		count += 1
		return count 
	return counter 
c1 = make_counter() 
c2 = make_counter() 
print(c1(), c1(), c2(), c2()) # Output: 1 1 1 1 
print(c1(), c2()) # Output: 2 2 


