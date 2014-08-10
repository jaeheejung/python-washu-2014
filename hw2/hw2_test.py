import unittest
from hw2 import *

class hw2Test(unittest.TestCase):
	def setUp(self):
		self.portfolio = Portfolio()
		
	def test_cash_transactions(self):
		self.assertEqual("cash: $300", self.portfolio.addCash(300))
		self.assertEqual("cash: -$50", self.portfolio.withdrawCash(50))
		self.assertEqual(["cash: $300", "cash: -$50"], self.portfolio.history)
		self.assertEqual({"cash": 250, "stock": {}, "mutual fund": {}}, self.portfolio.portfolio)
		print self.portfolio.portfolio_report
		
	def test_stock_transactions(self):
		self.portfolio.addCash(500)
		s1 = Stock(20, "HFH")
		s2 = Stock(7, "JHJ")
		self.assertEqual("stock: 5 HFH", self.portfolio.buyStock(5, s1))
		self.assertEqual("stock: 10 JHJ", self.portfolio.buyStock(10, s2))
		self.assertEqual(["cash: $500", "stock: 5 HFH", "stock: 10 JHJ"], self.portfolio.history)
		self.assertEqual({"cash": 330, "stock": {"HFH": 5, "JHJ": 10}, "mutual fund": {}}, self.portfolio.portfolio)
		self.assertEqual("stock: -1 HFH", self.portfolio.sellStock(s1, 1))
		self.assertEqual("stock: -2 JHJ", self.portfolio.sellStock(s2, 2))
		self.assertEqual(["cash: $500", "stock: 5 HFH", "stock: 10 JHJ", "stock: -1 HFH", "stock: -2 JHJ"], self.portfolio.history)
		print self.portfolio.portfolio_report
		
	def test_mutual_fund_transactions(self):
		self.portfolio.addCash(500)
		mf1 = MutualFund("BRT")
		mf2 = MutualFund("GHT")		
		self.assertEqual("mutual fund: 10 BRT", self.portfolio.buyMutualFund(10, mf1))
		self.assertEqual("mutual fund: 2 GHT", self.portfolio.buyMutualFund(2, mf2))
		self.assertEqual(["cash: $500", "mutual fund: 10 BRT", "mutual fund: 2 GHT"], self.portfolio.history)
		self.assertEqual({"cash": 488, "stock": {}, "mutual fund": {"BRT": 10, "GHT": 2}}, self.portfolio.portfolio)
		self.assertEqual("mutual fund: -3 BRT", self.portfolio.sellMutualFund(mf1, 3))
		self.assertEqual("mutual fund: -1 GHT", self.portfolio.sellMutualFund(mf2, 1))
		self.assertEqual(["cash: $500", "mutual fund: 10 BRT", "mutual fund: 2 GHT", "mutual fund: -3 BRT", "mutual fund: -1 GHT"], self.portfolio.history)
		print self.portfolio.portfolio_report

	def test_print_history(self):
		self.portfolio.addCash(500)
		s1 = Stock(20, "HFH")
		mf1 = MutualFund("BRT")
		self.assertEqual("stock: 5 HFH", self.portfolio.buyStock(5, s1))
		self.assertEqual("mutual fund: 10 BRT", self.portfolio.buyMutualFund(10, mf1))
		self.assertEqual("stock: -1 HFH", self.portfolio.sellStock(s1, 1))
		self.assertEqual("mutual fund: -3 BRT", self.portfolio.sellMutualFund(mf1, 3))
		print self.portfolio.historyRecord()

if __name__ == '__main__':
	unittest.main()
	
	
		