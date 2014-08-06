class Response():
	
	@classmethod
	def response(self, speak):	
		if "?" in speak:
			return "Sure."
		elif speak == speak.upper() and len(speak) != 0:
			return "Woah, chill out!"
		elif speak == "":
			return "Fine. Be that way!"
		else:
			return "Whatever."
	
	
	