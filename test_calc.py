
import unittest 
import seniorman

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(seniorman.add(10, 5), 15)
		self.assertEqual(seniorman.add(-1, 1), 0)
		self.assertEqual(seniorman.add(-1, -1), -2)

	def test_subtract(self):
		self.assertEqual(seniorman.subtract(10, 5), 5)
		self.assertEqual(seniorman.subtract(-1, 1), -2)
		self.assertEqual(seniorman.subtract(-1, -1), 0)

	def test_multiply(self):
		self.assertEqual(seniorman.multiply(10, 5), 50)
		self.assertEqual(seniorman.multiply(-1, 1), -1)
		self.assertEqual(seniorman.multiply(-1, -1), 1)

	def test_devide(self):
		self.assertEqual(seniorman.devide(10, 5), 2)
		self.assertEqual(seniorman.devide(-1, 1), -1)
		self.assertEqual(seniorman.devide(-1, -1), 1)

		with self.asserRaises(ValueError):
			calc.devide(10, 0)


if __name__== "__main__":
	unittest.main()