""" Tests our prime_numbers """

import unittest
from prime_numbers import prime

class Test_prime_numbers (unittest.Testcase):

	def test_value_is_number():
		self.asserEqual (self.prime ("one"), "Sorry! Only numbers allowed")

	def test_number_negatives():
		self.assertEqual (self.prime (-1), "Sorry! Prime numbers are positives")

	def test_number_positives():
		self.assertEqual (self.prime (3), True)
		self.assertEqual (self.prime (4), False)

	def test_number_is_whole():
		self.assertEqual (self.prime (float), "Sorry! Prime numbers are whole")
		self.assertEqual (self.prime (3.2), "Sorry! Prime numbers are whole")

		


