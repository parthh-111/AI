
import heapq

ROMANIA_MAP = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


class Node:
    def __init__(self, city, parent=None, g=0, h=0):
        self.city = city
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def a_star_search(start, goal):
    open_list = []

    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    closed_set = set()

    while open_list:

        current = heapq.heappop(open_list)

        if current.city == goal:
            path = []
            total_cost = current.g

            while current:
                path.append(current.city)
                current = current.parent

            return path[::-1], total_cost

        if current.city in closed_set:
            continue

        closed_set.add(current.city)

        for neighbor, cost in ROMANIA_MAP[current.city].items():

            if neighbor in closed_set:
                continue

            g = current.g + cost
            h = heuristic[neighbor]

            neighbor_node = Node(neighbor, current, g, h)

            skip = False

            for node in open_list:
                if node.city == neighbor and node.f <= neighbor_node.f:
                    skip = True
                    break

            if not skip:
                heapq.heappush(open_list, neighbor_node)

    return None, float('inf')


# Test A* Search
start = 'Arad'
goal = 'Bucharest'

path, cost = a_star_search(start, goal)

if path:
    print("Path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")

