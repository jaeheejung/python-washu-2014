import unittest
from quick_sort import *

class quickSortTest(unittest.TestCase):
	def test_sorting_numbers(self):
		self.assertEqual([4],quick_sort([4]))
		self.assertEqual([-7,-4,0,2,3,10,15],quick_sort([2,-4,0,10,15,-7,3]))
		
	def test_sorting_letters(self):
		self.assertEqual(["a"],quick_sort(["a"]))
		self.assertEqual(['C','E','T','b','c','k'],quick_sort(['T','C','c','k','E','b']))
	
	def test_sorting_symbols(self):
		self.assertEqual(["!"],quick_sort(["!"]))
		self.assertEqual(['*','>','?'],quick_sort(['?','*','>']))
		
	def test_sorting_mix(self):
		self.assertEqual([-6, 5, ',', '/', '?', 'K', 'c'],quick_sort(['/',',','c',5,-6,'K','?']))
		
if __name__ == '__main__':
	unittest.main()