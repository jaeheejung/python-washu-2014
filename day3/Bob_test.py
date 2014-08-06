import unittest
from Bob import *

class BobTest(unittest.TestCase):
	
	def test_ask_question(self):
		self.assertEqual("Sure.", Response.response("How are you?"))
		self.assertEqual("Sure.", Response.response("HOW ARE YOU?"))
	
	def test_yell(self):
		self.assertEqual("Woah, chill out!", Response.response("HOW COULD YOU!"))
		self.assertEqual("Woah, chill out!", Response.response("HOW COULD YOU."))
	
	def test_say_nothing(self):
		self.assertEqual("Fine. Be that way!", Response.response(""))
	
	def test_anything_else(self):
		self.assertEqual("Whatever.", Response.response("This is something else."))
		self.assertEqual("Whatever.", Response.response("This is something else!"))

if __name__ == '__main__':
	unittest.main()