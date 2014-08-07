class School():
	def __init__(self, school):
		self.school = school
		self.db = {}
	
	def add(self, name, grade):
		if grade in self.db.keys():  # To add a student to an existant grade
			self.db[grade].add(name)
		else:  # To add a student for the first time or to a non-existant grade
			self.db[grade] = {name}
		return self.db
	
	def grade(self, grade):
		if grade not in self.db.keys():  # To get students from a non-existant grade
			return None
		else:  # To get students from an existing grade
			return self.db[grade]
	
	def sort(self):
		for each_key in sorted(self.db.iterkeys()):
			self.db[each_key] = tuple(sorted(self.db[each_key]))
		return self.db