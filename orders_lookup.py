# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

class OrderHistory:
	_instance = None

	@staticmethod
	def getInstance():
		if OrderHistory._instance == None:
			OrderHistory()
		return OrderHistory._instance

	def __init__(self):
		if OrderHistory._instance != None:
			raise Exception("OrderHistory is a Singleton class")
		else:
			OrderHistory._instance = self
			self._order_ids = []

	def record(self, order_id):
		self._order_ids.append(order_id)

	def get_last(self, i):
		order_ids_len = len(self._order_ids)
		get_index = order_ids_len - i
		return self._order_ids[get_index]

orderHistory = OrderHistory.getInstance()
orderHistory.record("123")
orderHistory.record("124")
orderHistory.record("256")
assert orderHistory.get_last(1) == "256"
orderHistory.record("577")
orderHistory.record("999")
orderHistory.record("48")
assert orderHistory.get_last(1) == "48"
assert orderHistory.get_last(5) == "124"


