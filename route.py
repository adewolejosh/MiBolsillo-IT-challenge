
class Route:


	def _graph_input(self):
		graph = [entry for entry in input("Enter a list of graph entries : ").split(',')]
		return graph


	# dictionary of all feasible pair nodes and weights
	def _graph_dictionary(self, graph):
		dictionary = {}

		for j in range(len(graph)):
			cities_distances = graph[j].split()
			cities = list(cities_distances[0])

			dictionary[f'{cities[0]}{cities[1]}'] = f'{cities[2]}'

		return dictionary


	# list of all nodes available
	def _city(self, graph):
		pass


	# list of all feasible pair nodes
	def _city_list(self, graph):
		lists = []

		for j in range(len(graph)):
			cities_distances = graph[j].split()
			cities = list(cities_distances[0])

			lists.append(f'{cities[0]}{cities[1]}')

		return lists


	# function that outputs for standard route route
	def findstandardpath(self):
		route = input("Enter a path to find: ")
		graph = self._graph_input()
		route_list = route.split('-')
		distance = []
		dist_list = self._graph_dictionary(graph)
		city_list = self._city_list(graph)

		# check for each route splits
		# A-B-C-D-E
		for i in range(len(route_list)-1):
			city = str(route_list[i] + route_list[i+1])

			if city in city_list:
				for k, v in dist_list.items():
					if k == city:
						distance.append(int(v))

			else:
				return print("NO SUCH ROUTES")

		length = sum(distance)
		return print(length)


	# function that outputs trips through a certain path with maximum number of stops
	def findtripstoandfroapath(self):
		route = input("Enter two paths: ")
		maximum_stop = int(input("Enter the maximum no. of stop: "))


	def findshortestpath(self):
		route = input("Enter a route to find the shortest path: ")


	def finddifferentpaths(self):
		route = input("Enter the to and fro path: ")
