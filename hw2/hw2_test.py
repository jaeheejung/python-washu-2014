import unittest
from hw2 import *

class hw2Test(unittest.TestCase):
	def setUp(self):
		self.portfolio = Portfolio()
		
	def test_cash_transactions(self):
		self.assertEqual("cash: $300.00", self.portfolio.addCash(300))
		self.assertEqual("cash: -$50.00", self.portfolio.withdrawCash(50))
		self.assertEqual(["cash: $300.00", "cash: -$50.00"], self.portfolio.history)
		self.assertEqual({"stock": {}, "mutual fund": {}, "bond": {}}, self.portfolio.portfolio)
		self.assertEqual(250, self.portfolio.cash)
		self.portfolio.__str__()

	def test_stock_transactions(self):
		self.portfolio.addCash(500.50)
		s1 = Stock(20, "HFH")
		s2 = Stock(7, "JHJ")
		self.assertEqual("stock: 5.00 HFH", self.portfolio.buyStock(5, s1))
		self.assertEqual("stock: 10.00 JHJ", self.portfolio.buyStock(10.2, s2))
		self.assertEqual(["cash: $500.50", "stock: 5.00 HFH", "stock: 10.00 JHJ"], self.portfolio.history)
		self.assertEqual({"stock": {"HFH": 5, "JHJ": 10}, "mutual fund": {}, "bond": {}}, self.portfolio.portfolio)
		self.assertEqual(330.5, self.portfolio.cash)
		self.assertEqual("stock: -1.00 HFH", self.portfolio.sellStock(s1, 1))
		self.assertEqual("stock: -2.00 JHJ", self.portfolio.sellStock(s2, 2))
		self.assertEqual(["cash: $500.50", "stock: 5.00 HFH", "stock: 10.00 JHJ", "stock: -1.00 HFH", "stock: -2.00 JHJ"], self.portfolio.history)
		self.assertEqual({"stock": {"HFH": 4, "JHJ": 8}, "mutual fund": {}, "bond": {}}, self.portfolio.portfolio)
		self.portfolio.__str__()

	def test_mutual_fund_transactions(self):
		self.portfolio.addCash(500)
		mf1 = MutualFund(1, "BRT")
		mf2 = MutualFund(1, "GHT")		
		self.assertEqual("mutual fund: 10.00 BRT", self.portfolio.buyMutualFund(10, mf1))
		self.assertEqual("mutual fund: 2.00 GHT", self.portfolio.buyMutualFund(2, mf2))
		self.assertEqual(["cash: $500.00", "mutual fund: 10.00 BRT", "mutual fund: 2.00 GHT"], self.portfolio.history)
		self.assertEqual({"stock": {}, "mutual fund": {"BRT": 10, "GHT": 2}, "bond": {}}, self.portfolio.portfolio)
		self.assertEqual(488, self.portfolio.cash)
		self.assertEqual("mutual fund: -3.00 BRT", self.portfolio.sellMutualFund(mf1, 3))
		self.assertEqual("mutual fund: -1.00 GHT", self.portfolio.sellMutualFund(mf2, 1))
		self.assertEqual(["cash: $500.00", "mutual fund: 10.00 BRT", "mutual fund: 2.00 GHT", "mutual fund: -3.00 BRT", "mutual fund: -1.00 GHT"], self.portfolio.history)
		self.portfolio.__str__()
	
	def test_bond_transactions(self):
		self.portfolio.addCash(500.12)
		b1 = Bond(5.50, "IHK")
		b2 = Bond(7.30, "ESA")		
		self.assertEqual("bond: 10.20 IHK", self.portfolio.buyBond(10.2, b1))
		self.assertEqual("bond: 2.73 ESA", self.portfolio.buyMutualFund(2.73, b2))
		self.assertEqual(["cash: $500.12", "bond: 10.20 IHK", "bond: 2.73 ESA"], self.portfolio.history)
		self.assertEqual({"stock": {}, "mutual fund": {}, "bond": {"IHK": 10.2, "ESA": 2.73}}, self.portfolio.portfolio)
		self.assertEqual(424.09, self.portfolio.cash)
		self.assertEqual("bond: -3.10 IHK", self.portfolio.sellBond(b1, 3.1))
		self.assertEqual("bond: -1.00 ESA", self.portfolio.sellBond(b2, 1))
		self.assertEqual(["cash: $500.12", "bond: 10.20 IHK", "bond: 2.73 ESA", "bond: -3.10 IHK", "bond: -1.00 ESA"], self.portfolio.history)
		self.portfolio.__str__()
		
	def test_print_history(self):
		self.portfolio.addCash(500)
		s1 = Stock(20, "HFH")
		mf1 = MutualFund(1, "BRT")
		b1 = Bond(5.50, "IHK")
		self.assertEqual("stock: 5.00 HFH", self.portfolio.buyStock(5, s1))
		self.assertEqual("mutual fund: 10.00 BRT", self.portfolio.buyMutualFund(10, mf1))
		self.assertEqual("bond: 10.20 IHK", self.portfolio.buyBond(10.2, b1))
		self.assertEqual("stock: -1.00 HFH", self.portfolio.sellStock(s1, 1))
		self.assertEqual("mutual fund: -3.00 BRT", self.portfolio.sellMutualFund(mf1, 3))
		self.assertEqual("bond: -3.10 IHK", self.portfolio.sellBond(b1, 3.1))
		print self.portfolio.historyRecord()

if __name__ == '__main__':
	unittest.main()
	
	
		