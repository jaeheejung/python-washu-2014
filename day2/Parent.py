class Parent():
	def __init__(self, sex, firstname, lastname):
		self.sex = sex
		self.firstname = firstname
		self.lastname = lastname
		self.kids = []
	
	def role(self):
		if self.sex == "Male":
			return "Father"
		else:
			return "Mother"

	def have_child(self, name):
		print self.firstname + "is having a child named " + name
		print "They will make a very good " + self.role()
		child = Child("Jill", self) 
		self.kids.append(child)

class Child():
	def __init__(self, firstname, parent):
		self.parent = parent
		self.lastname = parent.lastname
		self.firstname = firstname
	
	def introduce(self):
		return "Hi I'm %s %s" % (self.firstname, self.lastname)

mom = Parent("Female", "Jane", "Smith")
mom.have_child("Jill")
		
	