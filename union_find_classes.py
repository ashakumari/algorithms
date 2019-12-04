# Time complexity O(N) for union and O(1) for find
class UF_arr:
	connected_components = []
		
	def __init__(self, n):
		self.connected_components = [i for i in range(n)]

	def union(self, p, q):
		value_of_p = self.connected_components[p]
		value_of_q = self.connected_components[q]
		
		self.connected_components[q] = value_of_p

		for i in range(len(self.connected_components)):
			if self.connected_components[i] == value_of_q:
				self.connected_components[i] = value_of_p

	def is_connected(self, p,q):
		return True if self.connected_components[p] == self.connected_components[q] else False

# Time complexity O(N) for union and O(N) for find
class UF_tree:
	connected_components = []
		
	def __init__(self, n):
		self.connected_components = [i for i in range(n)]

	def union(self, p, q):
		root_of_p = self.get_root(p)
		root_of_q = self.get_root(q)
		
		self.connected_components[root_of_q] = root_of_p
		
		print(self.connected_components)

	def get_root(self, r):
		current_node_id = r
		current_node_value = self.connected_components[r]

		while current_node_id != current_node_value:
			current_node_id = current_node_value
			current_node_value = self.connected_components[current_node_id]

		return current_node_id


	def is_connected(self, p,q):
		return True if self.get_root(p) == self.get_root(q) else False

# Time complexity O(logN) for union and O(logN) for find but O(N) additional space
class UF_wtree:
	connected_components = []
	weights = []
		
	def __init__(self, n):
		self.connected_components = [i for i in range(n)]
		self.weights = [1]*n

	def union(self, p, q):
		root_of_p = self.get_root(p)
		root_of_q = self.get_root(q)

		if self.weights[p] > self.weights[q]:
			self.connected_components[root_of_q] = root_of_p
			self.weights[root_of_p] += self.weights[root_of_q]
		else:
			self.connected_components[root_of_p] = root_of_q
			self.weights[root_of_q] += self.weights[root_of_p]
		
		print(self.connected_components)

	def get_root(self, r):
		current_node_id = r
		current_node_value = self.connected_components[r]

		while current_node_id != current_node_value:
			current_node_id = current_node_value
			current_node_value = self.connected_components[current_node_id]

		return current_node_id


	def is_connected(self, p,q):
		return True if self.get_root(p) == self.get_root(q) else False


