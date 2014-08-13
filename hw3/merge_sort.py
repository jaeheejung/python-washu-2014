def merge_sort(list_to_sort): 
	if len(list_to_sort) > 1:
		mid_index = len(list_to_sort) / 2  # Get the index for the middle of the list
		left = list_to_sort[:mid_index]  # Divide the list in half
		right = list_to_sort[mid_index:]  # Divide the list in half
		
		merge_sort(left)  # Recursively split the left side
		merge_sort(right)  # Recursively split the right side
		
		i, j, k = 0, 0, 0  # This block of code loops through the elements and merges them in increasing order
		while i < len(left) and j < len(right): 
			if left[i] < right[j]:
				list_to_sort[k] = left[i]
				i += 1
			else:
				list_to_sort[k] = right[j]
				j += 1
			k += 1
		while j < len(right):
			list_to_sort[k] = right[j]
			k += 1
			j += 1
		while i < len(left):
			list_to_sort[k] = left[i]
			k += 1
			i += 1
		return list_to_sort
	else:
		return list_to_sort
	
