#  graph input
graph = [entry for entry in input("Enter a list of graph entries : ").split(',')]

# function that outputs for route
def find(route):
	route_list = route.split('-')
	distance = []

	# check for each route splits
	# A-B-C-D-E
	for i in range(route_list-1):
		city = route_list[i]+route_list[i+1]

		for j in range(graph):
			dist = graph[j].split()

			for k in range(1):
				cities = dist[k] + dist[k+1]

				if city == cities:
					distance.append(dist[2])

	return sum(distance)