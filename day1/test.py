""" Tests our prime_numbers """

import unittest
from unittest import TestCase
from prime_numbers import prime

class Test_prime_numbers (unittest.TestCase):

	def test_value_is_number(self):
		self.asserEqual (self.prime ("one"), "Sorry! Only numbers allowed")

	def test_number_negatives(self):
		self.assertEqual (self.prime (-1), "Sorry! Prime numbers are positives")

	def test_number_positives(self):
		self.assertEqual (self.prime (3), True)
		self.assertEqual (self.prime (4), False)

	def test_number_is_whole(self):
		self.assertEqual (self.prime (float), "Sorry! Prime numbers are whole")
		self.assertEqual (self.prime (3.2), "Sorry! Prime numbers are whole")



		


