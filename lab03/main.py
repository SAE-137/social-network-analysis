
import networkx as nx
import matplotlib.pyplot as plt

n = 150
p = 0.15

G = nx.erdos_renyi_graph(n, p, seed=137)

degrees = [degree for node, degree in G.degree()]
average_degree = sum(degrees) / n

expected_degree = (n - 1) * p

print(f"Количество вершин: {G.number_of_nodes()}")
print(f"Количество рёбер: {G.number_of_edges()}")
print(f"Средняя степень: {average_degree:.4f}")
print(f"Теоретическая средняя степень: {expected_degree:.4f}")
print(f"Отклонение: {abs(average_degree - expected_degree):.4f}")

# Визуализация графа
plt.figure(figsize=(9, 7))

pos = nx.spring_layout(G, seed=137)

nx.draw(
    G,
    pos,
    node_size=40,
    with_labels=False,
    width=0.4,
    alpha=0.5
)

plt.show()
