class Senator():
	def __init__(self, name):
		self.name = name
	
	def vote(self, bill, choice):
		bill.votes[choice].append(self.name)
		

class Bill():
	def __init__(self, title):
		self.title = title
		self.votes = {"yes" : [], "no" : [], "abstain" : []}
	
	def result(self):
		if len(self.votes["yes"]) > len(self.votes["no"]):
			self.passed = True
		else:
			self.passed = False

jane = Senator("Jane")
jack = Senator("Jack")
environment = Bill("Environmental Protection")
jane.vote(environment, "yes")

print environment.votes