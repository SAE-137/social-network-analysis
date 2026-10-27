
from math import inf

graph = [
    [(1, 4), (2, 2)],
    [(0, 4), (2, 1), (3, 5)],
    [(0, 2), (1, 1), (3, 8)],
    [(1, 5), (2, 8)]
]

def dejkstra_(graph, start):

    distances = [inf] * len(graph)
    visited = [False] * len(graph)

    distances[start] = 0

    while True:
        min_distance = inf
        index_min = None
        for i in range(len(distances)):
            if distances[i] < min_distance and visited[i] == False:
                min_distance = distances[i]
                index_min = i
        if index_min == None:
            return distances

        visited[index_min] = True
        for index, distance in graph[index_min]:
            new_distance = distances[index_min] + distance 
            if  new_distance < distances[index]: 
                distances[index] = new_distance
            

print(dejkstra_(graph, 0))