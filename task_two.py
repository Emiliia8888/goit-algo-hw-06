import time
from collections import deque
from network_graph import create_security_network


def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    explored_order = []

    while queue:
        path = queue.popleft()
        node = path[-1]
        explored_order.append(node)

        if node == goal:
            return path, explored_order

        for neighbor in sorted(graph.neighbors(node)):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None, explored_order


def dfs_path(graph, start, goal, visited=None, path=None, explored_order=None):
    if visited is None:
        visited = {start}
    if path is None:
        path = [start]
    if explored_order is None:
        explored_order = []

    explored_order.append(start)

    if start == goal:
        return path, explored_order

    for neighbor in sorted(graph.neighbors(start)):
        if neighbor not in visited:
            visited.add(neighbor)
            result, explored_order = dfs_path(
                graph, neighbor, goal, visited, path + [neighbor], explored_order
            )
            if result:
                return result, explored_order

    return None, explored_order



def analyze(G):
    start = "Internet Gateway"
    goal = "Sensitive Database"

    # BFS
    bfs_start = time.perf_counter()
    bfs_result, bfs_explored = bfs_path(G, start, goal)
    bfs_time_ms = (time.perf_counter() - bfs_start) * 1000

    # DFS
    dfs_start = time.perf_counter()
    dfs_result, dfs_explored = dfs_path(G, start, goal)
    dfs_time_ms = (time.perf_counter() - dfs_start) * 1000

    print("Traversal results")
    print("-----------------")

    print("\nBFS path:")
    print(" -> ".join(bfs_result))
    print(f"Nodes explored (BFS): {len(bfs_explored)}")
    print(f"Exploration order (BFS): {bfs_explored}")
    print(f"Time taken (BFS): {bfs_time_ms:.4f} ms")

    print("\nDFS path:")
    print(" -> ".join(dfs_result))
    print(f"Nodes explored (DFS): {len(dfs_explored)}")
    print(f"Exploration order (DFS): {dfs_explored}")
    print(f"Time taken (DFS): {dfs_time_ms:.4f} ms")

    # DFS explores deeply along one departmental branch before considering others,
    # while BFS systematically examines all systems at increasing distances from
    # the gateway, reaching critical infrastructure sooner.

    # Even when BFS and DFS return the same solution path, BFS typically explores
    # fewer nodes because it expands the search frontier level by level and
    # terminates as soon as the goal is reached, whereas DFS may explore deep but
    # irrelevant branches before backtracking.

if __name__ == "__main__":
    G = create_security_network()
    analyze(G)
