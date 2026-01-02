import networkx as nx
from network_graph import create_security_network, visualize

G = create_security_network()
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()

degrees = [deg for _, deg in G.degree()]
avg_degree = sum(degrees) / num_vertices
max_degree = max(degrees)
min_degree = min(degrees)

print(f"Number of vertices (nodes): {num_vertices}")
print(f"Number of edges: {num_edges}")
print(f"Average degree: {avg_degree:.2f}")
print(f"Average clustering coefficient: {nx.average_clustering(G):.4f}")
print(f"Average shortest path length: {nx.average_shortest_path_length(G):.2f}")

visualize(G)