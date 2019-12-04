import union_find_classes as uf_module

def main():

	n = int(input("Enter the number of objects: "))
	uf = uf_module.UF_wtree(n)

	connect_more_components = 'y'

	while connect_more_components == 'y':

		pair_to_be_connected = input("Enter a pair of numbers separated by comma to be connected: ")
		p,q = (int(x) for x in pair_to_be_connected.split(","))

		if not uf.is_connected(p,q):
			uf.union(p,q)

		connect_more_components = input("Do you want to connect more objects (y/n)? ")

	find_more_connections = 'y'

	while find_more_connections == 'y':

		pair_to_check_for_connection = input("Enter a pair of numbers separated by comma to check if they are connected: ")
		p,q = (int(x) for x in pair_to_check_for_connection.split(","))

		if uf.is_connected(p,q):
			print("Yes. The two numbers {} and {} are connected.".format(p, q))
		else:
			print("No. The two numbers {} and {} are not connected.".format(p, q))

		find_more_connections = input("Do you want to check for more connected objects (y/n)? ")

main()

