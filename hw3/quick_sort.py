import random

def quick_sort(alist):
	if len(alist) <= 1:
		return alist
	else:
		index = random.randint(0, len(alist)-1)  # Get a random index for the pivot
		pivot = alist.pop(index)  # Take out and save the pivot from the list
	
		smaller = []
		larger = []
		for i in range(len(alist)):
			if alist[i] <= pivot:
				smaller.append(alist[i])  # Create a list of items smaller than the pivot
			else:
				larger.append(alist[i])  # Create a list of items larger than the pivot
	
		smaller = quick_sort(smaller)  # Recursion
		larger = quick_sort(larger)  # Recursion
		
		smaller.append(pivot)		
		alist = smaller + larger  # Combine the ordered lists
		
		return alist


	
	