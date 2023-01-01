#!/usu/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
	"""Divides all elements in a list


	Args:
		matrix: lists of lists of integers/floats
		div: a number (integer or float)

	Raises:
		TypeError: If elements in the lists are neither integers nor floats.
		TypeError: If rows in the matrix are not of the same size
		TypeError: If div is neither integer nor float
		ZeroDivisionError: If div == 0 

	Returns:
		A new matrix of elements divided by div
	"""
	if (not isinstance(matrix, list) or matrix == [] or
		not all(isinstance(row, list) for row in matrix) or
		not all((isinstance(element, int) or isinstance(element, float))
			for element in [num for row in matrix for num in row])):
	    raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
	
	if not all(len(row) == len(matrix[0]) for row in matrix):
	    raise TypeError("Each row of the matrix must have the same size")

	if not isinstance(div, int) and not isinstance(div, float):
	    raise TypeError("div must be a number")

	if div == 0:
	    raise ZeroDivisionError("division by zero")
	
	return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
