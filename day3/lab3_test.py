import unittest
import lab3

class lab3Test(unittest.TestCase):

	def setup(self):
		pass
	
	def test_shout(self):
		self.assertEqual("I'M FULL!", lab3.shout("I'm full."))
	
	def test_reverse(self):
		self.assertEqual("lluf", lab3.reverse("full"))
		
	def test_reversewords(self):
		self.assertEqual(".full I'm", lab3.reversewords("I'm full."))
	
	def test_reversewordletters(self):
		self.assertEqual("m'I lluf.", lab3.reversewordletters("I'm full."))
	
	def test_piglatin(self):
		self.assertEqual("esttay", lab3.piglatin("test"))
		
if __name__ == '__main__':
	unittest.main()