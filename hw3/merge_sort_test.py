import unittest
from merge_sort import *

class mergeSortTest(unittest.TestCase):
	def test_sorting_numbers(self):
		self.assertEqual([4],merge_sort([4]))
		self.assertEqual([-7,-4,0,2,3,10,15],merge_sort([2,-4,0,10,15,-7,3]))
		
	def test_sorting_letters(self):
		self.assertEqual(["a"],merge_sort(["a"]))
		self.assertEqual(['C','E','T','b','c','k'],merge_sort(['T','C','c','k','E','b']))
	
	def test_sorting_symbols(self):
		self.assertEqual(["!"],merge_sort(["!"]))
		self.assertEqual(['*','>','?'],merge_sort(['?','*','>']))
		
	def test_sorting_mix(self):
		self.assertEqual([-6, 5, ',', '/', '?', 'K', 'c'],merge_sort(['/',',','c',5,-6,'K','?']))
		
if __name__ == '__main__':
	unittest.main()