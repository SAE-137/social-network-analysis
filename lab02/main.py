
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for i in range(9):
    G.add_edge(i, i + 1)

G.add_edge(0, 7)

centrality = nx.eigenvector_centrality(G)

nodes = sorted(G.nodes())
values = [centrality[node] for node in nodes]

print("Количество вершин:", G.number_of_nodes())
print("Количество рёбер:", G.number_of_edges())

for node in nodes:
    print(f"Вершина {node}: {centrality[node]:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

pos = nx.spring_layout(G, seed=137)
nx.draw(
    G,
    pos,
    ax=axes[0],
    with_labels=True,
    node_color="lightblue",
    node_size=700,
    edge_color="gray",
    font_weight="bold"
)


axes[1].plot(nodes, values, marker="o")
axes[1].set_xticks(nodes)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
