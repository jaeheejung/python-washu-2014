def is_triangle(side1, side2, side3):
	if int(side1) > int(side2) + int(side3):
		print "No"
	elif int(side2) > int(side1) + int(side3):
		print "No"
	elif int(side3) > int(side1) + int(side2):
		print "No"
	else: print "Yes"

side1=raw_input("How long is side 1?")
side2=raw_input("How long is side 2?")
side3=raw_input("How long is side 3?")

is_triangle(side1,side2,side3)