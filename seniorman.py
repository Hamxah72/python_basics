
def add(x, y):
	"""Add Function"""
	return x + y


def subtract(x, y):
	"""Subtract Function"""
	return x - y


def multiply(x, y):
	"""Multiply Function"""
	return x * y


def devide(x, y):
	"""Devide Function"""
	if y == 0:
		raise ValueError("Can't devide by zero")
	return x // y


