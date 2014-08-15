class Node():
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next
		
	def __str__(self):
		return str(self.value)

class LinkedList():
	def __init__(self, value):  # O(1): Best possible complexity class
		if type(value) == int:  # I've restricted the list to take in only integers
			self.head =  Node(value)
			self.size = 1
		else:
			print "Input requires an integer"
	
	def length(self):  # O(1): Best possible complexity class
		return self.size  # self.size is appropriately adjusted in each method
	
	def addNode(self, new_value):  # O(n): Best possible complexity class
		current_node = self.head
		while current_node.next != None:  # Loop until a node has a pointer to a null next item
			current_node = current_node.next
		current_node.next = Node(new_value)  # Add the new node at the end
		self.size += 1

	def addNodeAfter(self, new_value, after_node):  # O(n): Best possible complexity class
		if after_node > self.size or after_node < 1:  # after_node cannot be a non-existant index
			print "Such a node does not exist"
		elif after_node == 1:  # When you want to add a new node after the head
			temp = self.head.next
			self.head.next = Node(new_value)
			self.head.next.next = temp
			self.size += 1
		else:  # When you want to add a new node after any node other than the head
			current_node = self.head
			index = 2
			while index <= after_node:		
				current_node = current_node.next
				index += 1
			current_node.next = Node(new_value, current_node.next)
			self.size += 1
	
	def addNodeBefore(self, new_value, before_node):  # O(n): Best possible complexity class
		if before_node > self.size or before_node < 1:  # before_node cannot be a non-existant index
			print "Such a node does not exist"
		elif before_node == 1:  # When you want to add a new node before the head and set it as the new head
			temp = Node(new_value)
			temp.next = self.head
			self.head = temp
			self.size += 1
		else:  # When you want to add a new node before any node other than the head
			current_node = self.head
			index = 2
			while index <= (before_node - 1):
				current_node = current_node.next
				index += 1
			current_node.next = Node(new_value, current_node.next)
			self.size += 1
	
	def removeNode(self, node_to_remove):  # O(n): Best possible complexity class
		if node_to_remove > self.size or node_to_remove < 1:  # You cannot remove a node that doesn't exist
			print "Such a node does not exist"
		elif node_to_remove == 1 and self.size == 1:  # When you try to remove the only node in the list
			print "You cannot remove the only node in the list"
		elif node_to_remove == 1:  # When you want to remove the head and set the next node as the new head
			self.head = self.head.next
			self.size -= 1
		elif node_to_remove == self.size:  # When you want to remove the tail
			current_node = self.head
			index = 2
			while index <= (node_to_remove - 1):
				current_node = current_node.next
				index += 1
			current_node.next = None
			self.size -= 1
		else:  # When you want to remove any node other than the head and the tail
			current_node = self.head
			index = 2
			while index <= node_to_remove:
				current_node = current_node.next
				index += 1
			current_node.value = current_node.next
			current_node.next = current_node.next.next
			self.size -= 1
					
	def removeNodesByValue(self, value):  # O(n): Best possible complexity class
		current_node = self.head
		index = 1
		while index <= self.size:
			if current_node.value == value:
				self.removeNode(index)
				if index == 1:  # When the value removed existed in the head
					current_node = self.head  # Reset current_node with the new head
				else:  # When the value removed existed in any node other than the head
					iter = 1
					current_node = self.head
					while iter <= (index - 1):  # Loop again from the head to arrive at the right current_node
						current_node = current_node.next
						iter += 1
			else:  # When the node is not the value you want to remove
				index += 1
				current_node = current_node.next
	
	def reverse(self):  # O(n): Best possible complexity class
		if self.size == 1:  # When the list has a single node, just leave it
			pass
		else:  # When the list has more than one node
			initial_size = self.size  # Remember the initial size of the list to reverse
			current_node = self.head
			iter = 1
			while iter <= initial_size:
				self.addNodeBefore(current_node.value,1)  # Extend the list in the front with the values in the list
				current_node = current_node.next
				iter += 1
			index = (self.size / 2) + 1
			while index <= self.size:
				self.removeNode(index)  # Remove the original part of the list
			
	def __str__(self):  # O(n): Best possible complexity class
		linked_list = "[%s" % (self.head)  # Open the list to print
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next
			linked_list += ","
			linked_list += str(current_node)
		linked_list += "]"  # Close the list to print
		return linked_list