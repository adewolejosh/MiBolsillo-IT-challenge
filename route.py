'''

N.B 
some words e.g path, node and city might be used interchangeably

'''

import itertools


class Route:

    def __init(self):
        # self.graph = [entry for entry in input("Enter a list of graph entries : ").split(',')]
        pass

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


    # list of all nodes available from graph entries
    def _city(self, graph):
        lists = []

        for j in range(len(graph)):
            cities_distances = graph[j].split()
            cities = list(cities_distances[0])
            a = cities[0]
            b = cities[1]
            
            if a not in lists: lists.append(a)
            elif b not in lists: lists.append(b)
            else: continue

        return lists


    # list of all feasible pair nodes
    def _city_list(self, graph):
        lists = []

        for j in range(len(graph)):
            cities_distances = graph[j].split()
            cities = list(cities_distances[0])

            lists.append(f'{cities[0]}{cities[1]}')

        return lists


    def _standardpath(self, route, graph):
        distance, dist_list, city_list = [], self._graph_dictionary(graph), self._city_list(graph)
        route_list = route.split('-')
        for i in range(len(route_list)-1):
            city = str(route_list[i] + route_list[i+1])

            if city in city_list:
                for k, v in dist_list.items():
                    if k == city:
                        distance.append(int(v))

            else:
                distance.append(0)

        if 0 in distance:
            return False
        else:
            return True



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
                return print("NO SUCH ROUTE")

        length = sum(distance)
        return print(length)


    # function that outputs trips through a certain path with maximum number of stops
    def findtripstoandfroapath(self, route=None, graph=None):
        route = route or input("Enter two paths: ")
        graph = graph or self._graph_input()
        maximum_stop = int(input("Enter the maximum no. of stop: "))
        exact_number = int(input("Enter the exact no. of stop: "))

        start_route = route.split()[0]
        end_route = route.split()[1]
        success = []

        # generate possible routes
        list_of_cities = self._city(graph)
        join_together = ''.join(list_of_cities)

        if maximum_stop != 0 and exact_number == 0:
            for i in range(maximum_stop):
                all_possible_routes = ['-'.join(x) for x in itertools.product(join_together, repeat=i)]

                for j in range(len(all_possible_routes)):
                    full_route = f'{start_route}-{all_possible_routes[j]}-{end_route}'

                    if self._standardpath(route=full_route, graph=graph) == True:
                        if full_route in success:
                            continue
                        else:
                            success.append(full_route)
                    else:
                        continue
        elif maximum_stop == 0  and exact_number != 0:
            all_possible_routes = ['-'.join(x) for x in itertools.product(join_together, repeat=exact_number)]

            for j in range(len(all_possible_routes)):
                full_route = f'{start_route}-{all_possible_routes[j]}-{end_route}'

                if self._standardpath(route=full_route, graph=graph) == True:
                    if full_route in success:
                        continue
                    else:
                        success.append(full_route)
                else:
                    continue


        return print(len(success))


    def findshortestpath(self, route=None, graph=None):
        route = route or input("Enter a route to find the shortest path: ")
        graph = graph or self._graph_input()
        result, distances = [], []


        start_route, end_route = route.split()[0], route.split()[1]
        list_of_cities = self._city(graph)
        join_together = ''.join(list_of_cities)

        # **************************************************************
        all_possible_routes = ['-'.join(x) for x in itertools.product(join_together, repeat=len())]

        ######################################################
        for j in range(len(all_possible_routes)):
            full_route = f'{start_route}-{all_possible_routes[j]}-{end_route}'

            if self._standardpath(route=full_route, graph=graph) == True:
                if full_route in result:
                    continue
                else:
                    result.append(full_route)
            else:
                continue
        #############################################################

        for i in range(len(result)):
            distances.append(self.findstandardpath(route=result[i]))

        minimum = min(distances)

        for j in distances:
            if distances[j] == minimum:
                return result[j]


    def finddifferentpaths(self):
        route = input("Enter the to and fro path: ")
