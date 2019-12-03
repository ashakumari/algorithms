# Queue implementation

class Queue:
	items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return None if len(self.items) == 0 else self.items.pop(0)

	def is_empty(self):
		return True if self.is_empty() else False


def parse_queue_string(str):
	que = Queue()
	result = ""
	
	for c in str:
		if c == '-':
			result += que.dequeue()
		else:
			que.enqueue(c)
	
	return result

assert parse_queue_string("1-2-3-4-5-") == "12345"
assert parse_queue_string("12345-----") == "12345"
assert parse_queue_string("12-34-5---") == "12345" 