#!/usr/bin/python3
"""Defines a function to add an integer"""

def add_integer(a, b=98):
	"""Returns an integer: the addition of a and b
	
	Floats args are typecasted to ints.

	Raises:
		TypeError: if either of a or b is not an int or a float.
	"""

	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))
		
	