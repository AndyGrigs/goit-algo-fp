import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

    def dijkstra(self, start):
        distances = [float('inf')] * self.vertices
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return distances

# Пример використання
graph = Graph(5)
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 2, 1) 
graph.add_edge(1, 3, 4)
graph.add_edge(2, 3, 2)
graph.add_edge(2, 4, 5)
graph.add_edge(3, 4, 6)

start_vertex = 0
distances = graph.dijkstra(start_vertex)
print(f"Найкоротші відстані від вершини {start_vertex} до інших вершин: {distances}")
