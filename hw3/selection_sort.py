def selection_sort(list_to_sort):
	for i in range(len(list_to_sort)):  # Each element of the list is used as the base element
		for j in range(i + 1, len(list_to_sort)):  # Across the rest of the list excluding the base element
			if list_to_sort[i] <= list_to_sort[j]:  # Pass if the later element is equal to or larger than the base element
				pass
			else:  # If the base element is larger than the later element
				temp = list_to_sort[j]  # Store the later element temporarily
				list_to_sort[j] = list_to_sort[i]  #Move the base element to the location of the later element
				list_to_sort[i] = temp  #Place the later element where the base element was
	return list_to_sort