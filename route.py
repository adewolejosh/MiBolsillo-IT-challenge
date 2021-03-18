
class Route:


	def graph_input(self):
		graph = [entry for entry in input("Enter a list of graph entries : ").split(',')]
		return graph


	def graph_dictionary(self, graph):
		dictionary = {}

		for j in range(len(graph)):
			cities_distances = graph[j].split()
			cities = list(cities_distances[0])

			dictionary[f'{cities[0]}{cities[1]}'] = f'{cities[2]}'

		return dictionary

	def city_list(self, graph):
		lists = []

		for j in range(len(graph)):
			cities_distances = graph[j].split()
			cities = list(cities_distances[0])

			lists.append(f'{cities[0]}{cities[1]}')

		return lists

	# function that outputs for route
	def findstandardpath(self, route=input("Enter a path to find: ")):
		graph = self.graph_input()
		route_list = route.split('-')
		distance = []
		dist_list = self.graph_dictionary(graph)
		city_list = self.city_list(graph)

		# check for each route splits
		# A-B-C-D-E
		for i in range(len(route_list)-1):
			city = str(route_list[i] + route_list[i+1])

			if city in city_list:
				for k, v in dist_list.items():
					if k == city:
						distance.append(int(v))

			else:
				return print("NO SUCH CITIES")

		length = sum(distance)
		return print(length)


if __name__ == '__main__':
	
	t = Route()
	t.findstandardpath()
