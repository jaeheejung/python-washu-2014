import random

class Portfolio():
	def __init__(self):
		self.cash = 0.00
		self.portfolio = {"stock": {}, "mutual fund": {}, "bond": {}}
		self.history = []
		
	def addCash(self, cash):
		self.cash += cash
		self.history.append("cash: $%.2f" % cash)
		return self.history[-1]

	def withdrawCash(self, cash):
		self.cash -= cash
		self.history.append("cash: -$%.2f" % (cash))
		return self.history[-1]

	def buyAsset(self, share, asset):
		self.share = share
		self.asset = asset
		self.cash -= self.asset.price * self.share
		self.cash = round(self.cash, 2)
		if self.asset.name in self.portfolio[self.asset.assetType()]:  # If the asset was purchased before
			(self.portfolio[self.asset.assetType()])[self.asset.name] += self.share
		else:  # If the asset is purchased for the first time
			(self.portfolio[self.asset.assetType()])[self.asset.name] = self.share
		self.history.append("%s: %.2f %s" % (self.asset.assetType(), self.share, self.asset.name))
		return self.history[-1]
	
	buyMutualFund = buyBond = buyAsset  # The buyAsset method works for both mutual funds and bonds
	
	def buyStock(self, share, asset):  # For stocks, make sure one can buy only whole units
		return self.buyAsset(int(share), asset)  

	def sellAsset(self, asset, share):
		self.asset = asset
		self.share = share
		self.cash += self.share * self.asset.sell_price
		self.cash = round(self.cash, 2)
		(self.portfolio[self.asset.assetType()])[self.asset.name] -= self.share
		self.history.append("%s: -%.2f %s" % (self.asset.assetType(), self.share, self.asset.name))
		return self.history[-1]
	
	sellMutualFund = sellBond = sellAsset  # The sellAsset method works for both mutual funds and bonds
	
	def sellStock(self, asset, share):  # For stocks, make sure one can sell only whole units
		return self.sellAsset(asset, int(share)) 
	
	def historyRecord(self):   # Print the history list in easy-to-read format
		return '\n'.join(self.history) 
	
	def __str__(self):  # Print the portfolio
		print "cash: $%.2f\n" % (self.cash) + ''.join('{}: {}\n'.format(key, val) for key, val in sorted(self.portfolio.items()))
		
class Stock(Portfolio):
	def __init__(self, price, name):
		Portfolio.__init__(self)
		self.price = price
		self.name = name
		self.sell_price = random.uniform(0.5 * self.price, 1.5 * self.price)
	
	def assetType(self):
		return "stock"
		
class MutualFund(Portfolio):
	def __init__(self, price, name):
		Portfolio.__init__(self)
		self.price = price
		self.name = name
		self.sell_price = random.uniform(0.9 * self.price, 1.2 * self.price)
		
	def assetType(self):
		return "mutual fund"

class Bond(Portfolio):
	def __init__(self, price, name):
		Portfolio.__init__(self)
		self.price = price
		self.name = name
		self.sell_price = random.uniform(0.7 * self.price, 1.3 * self.price)
		
	def assetType(self):
		return "bond"