class Burger():
	def __init__(self, filling, doneness, size, toppings, container):
		self.filling = filling
		self.doneness = doneness
		self.size = size
		if self.toppings_allowed(toppings):
			self.topping = toppings
		else:
			self.toppings = []
		self.toppings = toppings
		self.container = container
	
	def __str__(self):
		return "I'm a %s burger" % (self.doneness)
	
	def toppings_allowed(self, attempted_toppings):
		allowed_toppings = ["cheese", "tomato", "onion", "lettuce", "bacon"]
		for topping in attempted_toppings:
			if topping not in allowed_toppings:
				return False
		return True
		
	def tastiness(self):
		if "cheese" in toppings:
			return "VERY GOOD"
		elif self.doneness == "raw":
			return "yuck!"
	
	def cooking_time(self):
		# example sizes: 0.25, 0.33, 0.5
		# example doneness orderes: raw, rare, medium, well
		if self.doneness == "raw":
			time_for_doneness = 0
		elif self.doneness == "rare":
			time_for_doneness = 5
		elif self.doneness == "medium":
			time_for_doneness = 6
		elif self.doneness == "well":
			time_for_doneness = 8
		else:
			return "UNKNOWN"
		return self.size * 4 * time_for_doneness

# class VeggieBurger(Burger):
# 	def __init__(self, ):
# 		self.filling = "veggie patty"
		
rare_burger = Burger("beef", "rare", 0.25, ["cheese"], "bread")
print rare_burger.cooking_time()
print rare_burger