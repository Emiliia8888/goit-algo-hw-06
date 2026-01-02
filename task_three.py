import networkx as nx
from network_graph import create_security_network

def dijkstra_single_source(graph):
    start = "Internet Gateway"
    distances, paths = nx.single_source_dijkstra(graph, start, weight="weight")
    print("Shortest paths from Internet Gateway")
    print("-----------------------------------")
    for target in sorted(paths):
        path = paths[target]
        cost = distances[target]
        print(f"{start} -> {target} | Cost: {cost} | Path: {' -> '.join(path)}")

def dijkstra_all_pairs(graph):
    print("All-pairs shortest paths")
    print("------------------------")
    for source, (distances, paths) in nx.all_pairs_dijkstra(graph, weight="weight"):
        print(f"\nFrom {source}:")
        for target in paths:
            print(
                f"  To {target}: Cost = {distances[target]}, "
                f"Path = {' -> '.join(paths[target])}"
            )

if __name__ == "__main__":
    G = create_security_network()
    dijkstra_single_source(G)
    dijkstra_all_pairs(G)