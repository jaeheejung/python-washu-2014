import random

class Portfolio():
	def __init__(self):
		self.portfolio = {"cash": 0, "stock": {}, "mutual fund": {}}
		self.history = []
		
	def addCash(self, cash):
		self.cash = cash
		self.portfolio["cash"] += self.cash
		self.history.append("cash: $%d" % (self.cash))
		self.portfolio_report = ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		return self.history[-1]

	def withdrawCash(self, cash):
		self.cash = cash
		self.portfolio["cash"] -= self.cash
		self.history.append("cash: -$%d" % (self.cash))
		self.portfolio_report = ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		return self.history[-1]
		
	def buyStock(self, shares, stock):
		self.shares = shares
		self.stock = stock
		self.portfolio["cash"] -= self.stock.price * self.shares
		(self.portfolio["stock"])[self.stock.symbol] = self.shares
		self.history.append("stock: %d %s" % (self.shares, self.stock.symbol))
		self.portfolio_report = ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		return self.history[-1]

	def sellStock(self, stock, shares):
		self.stock = stock
		self.shares = shares
		stock_sell_price = random.uniform(0.5 * self.stock.price, 1.5 * self.stock.price)
		self.portfolio["cash"] += self.shares * stock_sell_price
		(self.portfolio["stock"])[self.stock.symbol] -= self.shares
		self.history.append("stock: -%d %s" % (self.shares, self.stock.symbol))
		self.portfolio_report = ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		return self.history[-1]
		
	def buyMutualFund(self, shares, mutual_fund):
		self.shares = shares
		self.mutual_fund = mutual_fund
		self.portfolio["cash"] -= self.shares
		(self.portfolio["mutual fund"])[self.mutual_fund.mutual_fund] = self.shares
		self.history.append("mutual fund: %d %s" % (self.shares, self.mutual_fund.mutual_fund))
		self.portfolio_report = ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		return self.history[-1]

	def sellMutualFund(self, mutual_fund, shares):
		self.mutual_fund = mutual_fund
		self.shares = shares
		mutual_fund_sell_price = random.uniform(0.9, 1.2)
		self.portfolio["cash"] += self.shares * mutual_fund_sell_price
		(self.portfolio["mutual fund"])[self.mutual_fund.mutual_fund] -= self.shares
		self.history.append("mutual fund: -%d %s" % (self.shares, self.mutual_fund.mutual_fund))
		self.portfolio_report = ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		return self.history[-1]
	
	def historyRecord(self):
		return '\n'.join(self.history)
		
class Stock(Portfolio):
	def __init__(self, price, symbol):
		Portfolio.__init__(self)
		self.price = price
		self.symbol = symbol
		
class MutualFund(Portfolio):
	def __init__(self, mutual_fund):
		Portfolio.__init__(self)
		self.mutual_fund = mutual_fund

class Bond(Portfolio):
	def __init__(self, price, name):
		Portfolio.__init__(self)
		self.price = price
		self.name = name