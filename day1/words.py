file = open('words.txt')

# for line in file:
#   word = line.strip()
#   print word
  
def has_no_e(string):
	return 'e' not in string
	
def uses_only(string, elements):
	return sorted(''.join(set(string))) == sorted(elements)

def uses_all(string, elements):
	return uses_only(string, elements)
	
def is_abecedarian(string):
	order = []
	for i in range(len(string)-1):
		order.append(string[i] <= string[i+1])
	if all(order) == True:
		return True
	else:
		return False
	
	