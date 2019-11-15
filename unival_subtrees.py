# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

def get_count_of_unival_subtrees(root):
	count, _ = check_for_unival_subtree(root)
	return count

def check_for_unival_subtrees(root):
	if root is None:
		return 0, True

	left_count, is_left_unival = check_for_unival_subtrees(root.left)
	right_count, is_right_unival = check_for_unival_subtrees(root.right)

	count = left_count + right_count
	is_unival = False

	if is_left_unival and is_right_unival:
		is_unival = True
		if root.left is not None and root.left.value != root.value:
			is_unival = False

		if root.right is not None and root.right.value != root.value:
			is_unival = False

		if is_unival == True:
			count += 1

	return count, is_unival


