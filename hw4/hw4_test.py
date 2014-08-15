import unittest
from hw4 import *

class hw4Test(unittest.TestCase):
	def test_input(self):
		LinkedList(None)
		LinkedList('a')
		LinkedList(20.34)
		LinkedList(5)
	
	def test_addNode(self):
		alist = LinkedList(5)
		alist.addNode(7)
		alist.addNode(5)
		alist.addNode(-10)
		self.assertEqual('[5,7,5,-10]',alist.__str__())
	
	def test_addNodeAfter(self):
		alist = LinkedList(0)
		alist.addNodeAfter(3,1)
		alist.addNodeAfter(-15,1)
		alist.addNodeAfter(17,3)
		self.assertEqual('[0,-15,3,17]',alist.__str__())
	
	def test_addNodeBefore(self):
		alist = LinkedList(-11)
		alist.addNodeBefore(8,1)
		alist.addNodeBefore(0,2)
		alist.addNodeBefore(50,3)
		alist.addNodeBefore(-17,4)
		self.assertEqual('[8,0,50,-17,-11]',alist.__str__())
	
	def test_removeNode(self):
		alist = LinkedList(99)
		alist.removeNode(1)
		alist.addNode(2)
		alist.addNode(16)
		alist.addNodeBefore(-77,1)
		alist.addNodeAfter(0,3)
		alist.removeNode(1)
		alist.removeNode(4)
		alist.removeNode(2)
		alist.removeNode(2)
		self.assertEqual('[99]',alist.__str__())
	
	def test_removeNodesByValue(self):
		alist = LinkedList(34)
		alist.addNode(-11)
		alist.addNode(-15)
		alist.addNodeBefore(30,1)
		alist.addNodeAfter(18,1)
		alist.addNodeAfter(30,1)
		alist.addNodeBefore(30,5)
		alist.addNodeAfter(30,7)
		self.assertEqual('[30,30,18,34,30,-11,-15,30]',alist.__str__())
		alist.removeNodesByValue(30)
		self.assertEqual('[18,34,-11,-15]',alist.__str__())
	
	def test_reverse(self):
		alist = LinkedList(31)
		alist.addNode(70)
		alist.addNode(-23)
		self.assertEqual('[31,70,-23]',alist.__str__())
		alist.reverse()
		self.assertEqual('[-23,70,31]',alist.__str__())
	
	def test_length(self):
		alist = LinkedList(9)
		alist.addNode(30)
		alist.addNodeAfter(-4,2)
		alist.addNodeBefore(-65,1)
		alist.removeNode(1)
		alist.removeNodesByValue(-4)
		self.assertEqual(2,alist.length())

if __name__ == '__main__':
	unittest.main()