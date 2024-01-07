
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
	def test_email(self):
		emp_1 = Employee("Addul", "Fideh", 50000)
		emp_2 = Employee("Muhammad", "Ardo", 60000)

		self.assertEqual(emp_1.email, "Abdul.Fideh@gamil.com")
		self.assertEqual(emp_2.email, "Muhammad.Fideh@gamil.com")

		emp_1.first = "Hamza"
		emp_2.first = "Umar"


		self.assertEqual(emp_1.email, "Hamza.Fideh@gamil.com")
		self.assertEqual(emp_2.email, "Umar.Fideh@gamil.com")


	def test_fullname(self):
		emp_1 = Employee("Addul", "Fideh", 50000)
		emp_2 = Employee("Muhammad", "Ardo", 60000)

	