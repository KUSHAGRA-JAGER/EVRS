import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def add_node(self, value):
        self.nodes.add(value)a
        self.edges[value] = []
        
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))

def dijkstra(graph, start, end):
    shortest_paths = {node: (float('inf'), []) for node in graph.nodes}
    shortest_paths[start] = (0, [start])

    pq = [(0, start)]

    while pq:
        (current_distance, current_node) = heapq.heappop(pq)

        if current_distance > shortest_paths[current_node][0]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_node][1] + [neighbor])
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths[end]

# graph (city map)
city_map = Graph()
locations = ["Hospital", "Junction1", "Junction2", "Junction3", "AccidentSite", "PoliceStation"]

for loc in locations:
    city_map.add_node(loc)

# roads (edges) and distances (in km)
roads = [
    ("Hospital", "Junction1", 4),
    ("Junction1", "Junction2", 3),
    ("Junction2", "AccidentSite", 6),
    ("Hospital", "Junction3", 5),
    ("Junction3", "AccidentSite", 2),
    ("PoliceStation", "Junction2", 4)
]

for road in roads:
    city_map.add_edge(*road)

# input
start = input("Enter emergency vehicle current location (e.g., Hospital): ").strip()
end = input("Enter emergency site location (e.g., AccidentSite): ").strip()

# run
if start in city_map.nodes and end in city_map.nodes:
    distance, path = dijkstra(city_map, start, end)
    print(f"\n Shortest route from {start} to {end}: {' -> '.join(path)}")
    print(f" Total distance: {distance} km")
else:
    print("Invalid locations entered. Please check the names and try again.")
