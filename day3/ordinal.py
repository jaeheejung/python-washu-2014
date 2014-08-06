def ordinal(n):
	negative = False
	try:
		n = int(n) # If error occurs here, return below
	except:
		return "Improper input"
	if n < 0:
		n = abs(n)
		negative = True
	last_digit = n % 10
	second_to_last_digit = (n % 100) / 10
	endings = {1: "st", 2: "nd", 3: "rd"}
	ending = "th"
	if second_to_last_digit != 1 and last_digit in endings.keys():
		ending = endings[last_digit]
	if negative:
		n = -n
	return str(n) + ending