class BiologicalThing(object):
	def alive(self):
		return True

class Animal(BiologicalThing):
	def __init__(self, age): # initializer or constructor
		self.age = age
		
	def gets_energy_directly_from_the_sun(self):
		return False

class Plant(BiologicalThing):
	def gets_energy_directly_from_the_sun(self):
		return True

class Mammal(Animal):
	def __init__(self, age, sex):
		Animal.__init__(self, age)
		self.sex = sex
		
	def has_hair(self):
		return True

	def has_live_births(self):
		return True

class Human(Mammal): # class definition # you don't have to write out object
	def __init__(self, age, sex, name): # initializer or constructor
		Mammal.__init__(self, age, sex)
		self.name = name
	
	def speak(self, words):
		if self.sex == "Male":
			return words.upper()
		else:
			return words
	
	def introduce(self):
		return self.speak("Hello, I'm %s" % self.name)
	
	def reveal_age(self):
		if self.sex == "Male":
			return self.speak("I'm %d" % self.age)
		else:
			return "Don't you know better?"
		
andy = Human(21, "Male", "Andy")
print andy.introduce()
print andy.reveal_age()
print andy.gets_energy_directly_from_the_sun()
print dir(andy)

betul = Human("impolite to ask", "Female", "Betul")
print betul.introduce()
print betul.reveal_age()