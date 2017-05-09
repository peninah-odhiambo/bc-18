""" Tests our prime_numbers """

import unittest
from unittest import TestCase
from prime_numbers import prime

class Test_prime_numbers (unittest.TestCase):

	""" Checks if value given is number"""
	def test_value_is_number(self):
		self.asserEqual (self.prime ("one"), "Sorry! Only numbers allowed")

	""" Checks is number given is negative """
	def test_number_negatives(self):
		self.assertEqual (self.prime (-1), "Sorry! Prime numbers are positives")

	""" Checks if number given is positive """
	def test_number_positives(self):
		self.assertEqual (self.prime (3), True)
		self.assertEqual (self.prime (4), False)

	""" Checks if number given is whole """
	def test_number_is_whole(self):
		self.assertEqual (self.prime (type (float)), "Sorry! Prime numbers are whole")

	""" Checks if an entry has been made """
	def test_number_given (self):
		self.assertEqual (self.prime (None), "Please make an entry")

	def test_correct_prime (self):
		self.assertEqual (self.prime (10), False)
		self.assertEqual (self.prime (7), True)

	""" Checks prime numbers for 15 and below """
	def test_number_upto_10(self):
		self.assertEqual (prime_numbers.self.prime (15), [2, 3, 5, 7, 11, 13])
	