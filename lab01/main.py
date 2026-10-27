
from math import inf


graph = [
    [(1, 4), (2, 2)],
    [(0, 4), (2, 1), (3, 5)],
    [(0, 2), (1, 1), (3, 8)],
    [(1, 5), (2, 8)]
]


def dijkstra(graph, start):
    if not 0 <= start < len(graph):
        raise ValueError("Начальная вершина не существует")

    distances = [inf] * len(graph)
    visited = [False] * len(graph)
    previous = [None] * len(graph)

    distances[start] = 0

    while True:
        min_distance = inf
        index_min = None

        for i in range(len(graph)):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                index_min = i

        if index_min is None:
            break

        visited[index_min] = True

        # Обновление расстояний до соседей
        for neighbor, weight in graph[index_min]:
            if weight < 0:
                raise ValueError("Отрицательные веса не допускаются")

            new_distance = distances[index_min] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = index_min

    return distances, previous


def restore_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)

        if current == start:
            return path[::-1]

        current = previous[current]

    return []


if __name__ == "__main__":
    start = 0

    distances, previous = dijkstra(graph, start)

    print(f"Начальная вершина: {start}\n")

    for vertex, distance in enumerate(distances):
        if distance == inf:
            print(f"Вершина {vertex}: путь отсутствует")
            continue

        path = restore_path(previous, start, vertex)
        path_str = " -> ".join(map(str, path))

        print(
            f"Вершина {vertex}: "
            f"путь {path_str}, расстояние {distance}"
        )
