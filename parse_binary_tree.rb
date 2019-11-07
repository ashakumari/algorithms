# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node
	attr_accessor :value, :left, :right
	
	def initialize(value, left=nil, right=nil)
		self.value = value
		self.left = left
		self.right = right
	end

	def to_s
		str = "{:value => '" + self.value + "'"
		unless self.left.nil?
			str += ", :left => #{self.left.to_s}"
		end
		unless self.right.nil?
			if self.left.nil?
				str += ", :left => ''"
			end
			str += ", :right => #{self.right.to_s}"
		end
		str += "}"
		return str
	end
end


def serialize(obj)
	return '' if obj.nil?
	return obj.to_s
end

def deserialize(s)
	eval s
end

test_node = Node.new('root', Node.new('left', Node.new('left.left')), Node.new('right'))

serialized_node = serialize(test_node)
deserialized_node = deserialize(serialized_node)

print deserialized_node[:left][:left][:value] == 'left.left'

